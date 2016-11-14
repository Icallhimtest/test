# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import math

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Tournament(models.Model):
    _name = "tournament"
    _order = 'id desc'
    # will inherit mail.thread prolly

    name = fields.Char(string='Tournament Name')
    match_type = fields.Selection([
        ('basic', 'Basic'),
        ('sets', 'Sets')], string='Match Type', readonly=True, states={'draft': [('readonly', False)]},
        help='How matches are won:\n' # TODO fix this display shit \t,n doesn't work
             '\tBasic: basic win - lose'
             '\tSets: matches are won by winning a certain number of sets')
    sets_to_win = fields.Integer(string='Sets to win', default=2, readonly=True, states={'draft': [('readonly', False)]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('done', 'Done')], default='draft', string='Tournament State')

    # schedule related fields
    time_organisation = fields.Boolean(string='Schedule the Matches', help='If checked, all matches will have a starting time.')
    start_date = fields.Datetime(string='Start Date')
    # maybe add date end and second start to handle 2-day events (weekends)
    avg_match_time = fields.Integer(string='Estimated Match Time', readonly=True, states={'draft': [('readonly', False)]})
    adapt_schedule = fields.Boolean(
        string='Adaptive start times',
        help='If checked, estimated match start time will automatically be adapted according to the current delay/advance.')
    field_amount = fields.Integer(
        string='Number of Fields', readonly=True, states={'draft': [('readonly', False)]},
        help='Number of matches that can be played at the same time.')

    # might need to create individual teams automatically for usability...
    players_per_team = fields.Integer(
        string='Players per team', readonly=True, states={'draft': [('readonly', False)]},
        help='Number of players in every team, leave empty or 0 for various size')
    team_ids = fields.Many2many('tournament.team', string='Participating Teams', readonly=True, states={'open': [('readonly', False)]})
    number_of_teams = fields.Integer(string='Number of Participating Teams', compute='_compute_number_of_teams', store=True, readonly=True)
    winner_id = fields.Many2one('tournament.team', string='Winner', readonly=True) # track
    runner_up_id = fields.Many2one('tournament.team', string='Runner up', readonly=True)
    match_ids = fields.One2many('tournament.match', 'tournament_id', string='Matches')

    @api.depends('team_ids')
    def _compute_number_of_teams(self):
        for tournament in self:
            tournament.number_of_teams = len(tournament.team_ids)

    def action_reset_to_draft(self):
        self.ensure_one()
        match_removal_list = []
        if self.match_ids:
            # TODO ask confirmation to delete all previous match data
            match_removal_list = [(2, match_id, 0) for match_id in self.match_ids.ids]
        self.write({'state': 'draft', 'winner_id': False, 'runner_up_id': False, 'match_ids': match_removal_list})

    def action_open(self):
        self.ensure_one()
        if self.match_type == 'sets' and self.sets_to_win <= 0:
            raise UserError(_('Number of sets to win must be positive'))
        if self.time_organisation and self.field_amount <= 0:
            raise UserError(_('Number of fields must be positive'))
        self.write({'state': 'open'})

    def action_close(self):
        """ Generates all the matches according to requested settings and the corresponding tree linking them together.
            if matches already exist (the tournament was reset to draft) warn that it will delete all existing matches.
        """
        self.ensure_one()
        self._verify_players_per_team()
        self._verify_players_unicity()
        number_of_rounds = int(math.ceil(math.log(self.number_of_teams, 2)))
        if number_of_rounds < 1:
            raise UserError(_('Not enough Participants'))
        match_ids = []
        for round_number in range(number_of_rounds):
            for i in range(2 ** round_number):
                # check if this works, or if I have to go through (0, 0, vals)
                match = self.env['tournament.match'].create({
                    'tournament_id': self.id,
                    'match_round': -round_number,
                    'set_ids': [(4, self.env['tournament.set'].create({}).id, 0)] if self.match_type == 'sets' else [],
                })
                match_ids.append(match.id)
                if round_number > 0:
                    match.next_match_id = match_ids[(match_ids.index(match.id) - 1) / 2]

        #assign teams to matches
        team_ids = self.team_ids.ids
        i = 0
        for match_id in match_ids[(2 ** (number_of_rounds - 1) - 1):]:
            match = self.env['tournament.match'].browse(match_id)
            match.first_team_id = self.env['tournament.team'].browse(team_ids[i])
            if self.number_of_teams > 2 ** (number_of_rounds - 1) + i:
                match.second_team_id = self.env['tournament.team'].browse(team_ids[2 ** (number_of_rounds - 1) + i])

        self.write({'state': 'closed'})

    def _verify_players_unicity(self):
        self.ensure_one()
        player_list = []
        for team in self.team_ids:
            player_list += team.player_ids.ids
        if len(player_list) != len(set(player_list)):
            duplicate_ids = [x for x in set(player_list) if player_list.count(x) >= 2] # TODO optimise this shit and imp the error msg
            raise UserError(_('Player %s is present in multiple teams') % self.env['res.partner'].browse(duplicate_ids[0]).name)

    def _verify_players_per_team(self):
        self.ensure_one()
        if self.players_per_team:
            for team in self.team_ids:
                if team.number_of_players != self.players_per_team:
                    raise UserError(_('Team %s does not have the required amount of players') % team.name)

    @api.depends('winner_id')
    def action_done(self):
        for tournament in self.filtered('winner_id'):
            tournament.write({'state': 'done'})


class TournamentTeam(models.Model):
    _name = "tournament.team"

    def _default_tournament_ids(self):
        if 'default_tournament_id' in self._context:
            return [(4, self._context.get('default_tournament_id'), 0)]

    name = fields.Char(string='Name', compute='_compute_name', store=True)
    player_ids = fields.Many2many('res.partner', string='Players') # TODO: create res.partner inheritance.
    tournament_ids = fields.Many2many('tournament', string='Participated Tournaments', readonly=True, default=_default_tournament_ids)
    number_of_players = fields.Integer(string='Number of Players', compute='_compute_number_of_players', readonly=True, store=True)

    @api.depends('player_ids')
    def _compute_number_of_players(self):
        for team in self:
            # import ipdb;ipdb.set_trace()
            team.number_of_players = len(team.player_ids)

    @api.depends('player_ids')
    def _compute_name(self):
        for team in self:
            # import ipdb;ipdb.set_trace()
            if not team.player_ids:
                team.name = 'Empty Team'
            else:
                result = ""
                for player in team.player_ids:
                    result += player.name.split(' ', 1)[0] + ", "
                team.name = result

    #name_get method or computed name


class TournamentMatch(models.Model):
    _name = "tournament.match"

    # # name_get method
    # def _default_tournament_id(self):
    #     if 'default_tournament_id' in self._context:
    #         return self._context.get('default_tournament_id')

    tournament_id = fields.Many2one('tournament', string='Tournament', required=True, readonly=True)
    first_team_id = fields.Many2one('tournament.team', string='Team 1', readonly=True)
    second_team_id = fields.Many2one('tournament.team', string='Team 2', readonly=True)
    set_ids = fields.One2many('tournament.set', 'match_id', string='Score')
    winner_id = fields.Many2one('tournament.team', string='Winner', readonly=True)
    match_round = fields.Integer(string='Round', help='Rounds go from -x to 0 for the final', readonly=True)
    next_match_id = fields.Many2one('tournament.match', string='Next Match', readonly=True)
    color = fields.Integer(string='Color Index')

    start_date = fields.Datetime(string='Start Date', compute='_compute_start_date', store=True)

    def _compute_start_date(self):
        pass

    def assign_winner(self, team):
        self.ensure_one()
        if self.tournament_id.match_type == 'basic':
            self.winner_id = self.first_team_id if team == 1 else self.second_team_id

    def check_result(self):
        """ Looks at the score of the sets (from set_ids) and assigns a winner if enough sets are played.
            If not enough sets were played, add a new set.
            If too many (due to score modification) remove unnecessary sets.
            If a winner is assigned, pass him on to the next round and assign tournament winner/runner-up if match was a final.
        """
        self.ensure_one()
        team_1_won = team_2_won = 0
        self.winner_id = False
        for set_id in self.set_ids:
            if self.winner_id:
                self.set_ids = [(2, set_id.id, 0)] # To Test, might mess up the iteration
            else:
                if set_id.score_1 >= set_id.score_2:
                    team_1_won += 1
                if set_id.score_1 <= set_id.score_2:
                    team_2_won += 1
                if max(team_1_won, team_2_won) == self.tournament_id.sets_to_win:
                    self.winner_id = self.first_team_id if team_1_won >= team_2_won else self.second_team_id
        if not self.winner_id:
            self.set_ids = [(0, 0, {})]
        else:
            self.prepare_next_match()

    def prepare_next_match(self):
        """ A winner is assigned, he passes on to the next round or, if the match
            was the final, declare the winner and runner-up of the tournament.
        """
        self.ensure_one()
        if not self.next_match_id:
            self.tournament_id.winner_id = self.winner_id
            self.tournament_id.runner_up_id = self.first_team_id.id ^ self.winner_id.id ^ self.second_team_id.id
        else:
            if not self.next_match_id.first_team_id:
                self.next_match_id.first_team_id = self.winner_id
            else:
                self.next_match_id.second_team_id = self.winner_id


class TournamentSet(models.Model):
    _name = "tournament.set"

    score_1 = fields.Integer(string='Team 1 score')
    score_2 = fields.Integer(string='Team 2 score')
    match_id = fields.Many2one('tournament.match', string='Match')

    @api.onchange('score_1', 'score_2')
    def _onchange_score_2(self):
        if self.score_1 and self.score_2:
            self.match_id.check_result()


class Partner(models.Model):
    _inherit = 'res.partner'

    team_ids = fields.Many2many('tournament.team', string='Tournament Teams', readonly=True)
