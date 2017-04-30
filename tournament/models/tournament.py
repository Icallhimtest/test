# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from dateutil.relativedelta import relativedelta
# import json
import math
import random

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class Tournament(models.Model):
    _name = "tournament"
    _order = 'id desc'
    # will inherit mail.thread prolly

    name = fields.Char(string='Tournament Name', required=True)
    match_type = fields.Selection([
        ('basic', 'Basic'),
        ('sets', 'Sets')], string='Match Type', readonly=True, states={'draft': [('readonly', False)]}, required=True, default='basic',
        help='How matches are won:\n' # TODO fix this display shit \t,n doesn't work
             '\tBasic: basic win - lose'
             '\tSets: matches are won by winning a certain number of sets')
    sets_to_win = fields.Integer(string='Sets to Win', default=2, readonly=True, states={'draft': [('readonly', False)]},
                                 help='Number of sets a player needs to win the match.')
    points_per_set = fields.Integer(string='Points per Set', default=21, readonly=True, states={'draft': [('readonly', False)]},
                                    help='Number of points a player needs to win the set.')
    # two_point_difference = fields.Boolean(string='2-Point Difference', default=True, readonly=True, states={'draft': [('readonly', False)]},
    #                                 help='Forces a 2-point difference to win a set.')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('done', 'Done')], default='draft', string='Tournament State', required=True, readonly=True,
        help="""State of the tournament:
                \tDraft = configuring the tournament
                \tOpen = open for registrations
                \tClosed = registrations closed
                \tDone = all matches have been played and a winner is proclaimed""")

    # schedule related fields
    # need verification to check every field required (according to settings) is set correctly
    time_organisation = fields.Boolean(string='Schedule the Matches', help='Check this to have match start times generated automatically.')
    # concurrent_tournaments = fields.Many2many(
    #     'tournament', string='Concurrent Tournaments', domain=[('state', 'in', ['draft', 'open'])],
    #     states={'closed': [('readonly', True)], 'done': [('readonly', True)]},
    #     help="Other tournaments that might have the same participant(s) playing in them, "
    #          "for which you want to avoid match time conflicts. "
    #          "Those tournaments need to be in draft mode.")
    date_range_ids = fields.One2many('tournament.date.range', 'tournament_id', string='Play Dates', help='Time periods matches can be played in.')
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
    description = fields.Text('Additional Information')

    @api.depends('team_ids')
    def _compute_number_of_teams(self):
        for tournament in self:
            tournament.number_of_teams = len(tournament.team_ids)

    @api.multi
    def write(self, values):
        if values.get('winner_id'):
            values.update({'state': 'done'})
        return super(Tournament, self).write(values)

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
        tournaments_to_close = self
        if self.time_organisation:
            tournaments_to_close |= self.concurrent_tournaments
        tournaments_to_close.generate_matches()
        tournaments_to_close.write({'state': 'closed'})

    def generate_matches(self):
        """ Generates all the matches according to requested settings and the corresponding tree linking them together.
            if matches already exist (the tournament was reset to draft) warn that it will delete all existing matches.
        """
        for tournament in self:
            tournament._verify_players_per_team()
            tournament._verify_players_unicity()
            number_of_rounds = int(math.ceil(math.log(tournament.number_of_teams, 2)))
            if number_of_rounds < 0:
                raise UserError(_('Not enough Participants for %s') % tournament.name)
            if tournament.time_organisation:
                tournament._verify_timing_possible(number_of_rounds)
            match_ids = []
            for round_number in range(number_of_rounds):
                for i in range(2 ** round_number):
                    # check if this works, or if I have to go through (0, 0, vals)
                    match = self.env['tournament.match'].create({
                        'tournament_id': tournament.id,
                        'match_round': -round_number,
                        'score': '[]',
                    })
                    match_ids.append(match.id)
                    if round_number > 0:
                        match.next_match_id = match_ids[(match_ids.index(match.id) - 1) / 2] #could be optimized by deducing index but shouldn't care

            # assign teams to matches
            team_ids = tournament.team_ids.ids
            random.shuffle(team_ids)
            i = 0
            for match_id in match_ids[(2 ** (number_of_rounds - 1) - 1):]:
                match = self.env['tournament.match'].browse(match_id)
                match.first_team_id = self.env['tournament.team'].browse(team_ids[i])
                if tournament.number_of_teams > 2 ** (number_of_rounds - 1) + i:
                    match.second_team_id = self.env['tournament.team'].browse(team_ids[2 ** (number_of_rounds - 1) + i])
                i += 1
            self.env['tournament.match'].browse(match_ids).write({'state': 'confirmed'})

    def _verify_players_unicity(self):
        player_list = []
        for team in self.team_ids:
            player_list += team.player_ids.ids
        if len(player_list) != len(set(player_list)):
            duplicate_ids = [x for x in set(player_list) if player_list.count(x) >= 2] # TODO optimise this shit and imp the error msg
            raise ValidationError(_('Player "%s" is present in multiple teams') % self.env['res.partner'].browse(duplicate_ids[0]).name)

    def _verify_players_per_team(self):
        if self.players_per_team:
            for team in self.team_ids:
                if team.number_of_players != self.players_per_team:
                    raise UserError(_('Team "%s" does not have the required amount of players') % team.name)

    def _verify_timing_possible(self, number_of_rounds):
        # to improve with # fields (and imp message)
        max_rounds = [int(d_range.duration * 60 / self.avg_match_time) for d_range in self.date_range_ids]
        if number_of_rounds > max_rounds:
            raise UserError(_('Tournament %s does not have enough play time') % self.name)

    # @api.depends('winner_id') where do you come from ?
    def action_done(self):
        for tournament in self.filtered('winner_id'):
            tournament.write({'state': 'done'})


class TournamentDateRange(models.Model):
    _name = "tournament.date.range"

    start = fields.Datetime(string='From', default=fields.Datetime.now)
    end = fields.Datetime(string='To')
    duration = fields.Float(string='Duration (hours)', computed='_compute_duration')
    tournament_id = fields.Many2one('tournament', string='related tournament', ondelete='cascade')

    @api.depends('start', 'end')
    def _compute_duration(self):
        difference = fields.Datetime.from_string(self.end) - fields.Datetime.from_string(self.start)
        self.duration = difference.hours + difference.minutes / 60.0

    @api.onchange('start')
    def _onchange_start(self):
        self.end = fields.Datetime.to_string(fields.Datetime.from_string(self.start) + relativedelta(hours=8))

    # check if the onchange triggers before when we change the start date. or if always valid.error
    @api.constrains('start', 'end')
    def _check_start_before_end(self):
        if self.end <= self.start:
            raise ValidationError(_('"To" datetime needs to be after the "From" datetime.'))
