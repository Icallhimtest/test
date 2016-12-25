# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import math
import random

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class TournamentMatch(models.Model):
    _name = "tournament.match"

    # # name_get method
    # def _default_tournament_id(self):
    #     if 'default_tournament_id' in self._context:
    #         return self._context.get('default_tournament_id')

    tournament_id = fields.Many2one('tournament', string='Tournament', required=True, readonly=True)
    match_type = fields.Selection(related='tournament_id.match_type', readonly=True)
    points_per_set = fields.Integer(related='tournament_id.points_per_set')
    first_team_id = fields.Many2one('tournament.team', string='Team 1', readonly=True)
    second_team_id = fields.Many2one('tournament.team', string='Team 2', readonly=True)
    score = fields.Text(string='Score', default='[]') # need to make widget
    winner_id = fields.Many2one('tournament.team', compute='_compute_winner_id', string='Winner', readonly=True, store=True)
    match_round = fields.Integer(string='Round', help='Rounds go from -x to 0 for the final', readonly=True)
    next_match_id = fields.Many2one('tournament.match', string='Next Match', readonly=True)
    previous_match_ids = fields.One2many('tournament.match', 'next_match_id', string='Previous Matches', readonly=True)
    color = fields.Integer(string='Color Index', compute="_compute_color")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('started', 'Started'),
        ('done', 'Done')], string='Match status', required=True, default='draft')

    start_date = fields.Datetime(string='Start Date', compute='_compute_start_date', store=True)

    def _compute_start_date(self):
        if self.tournament_id.time_organisation:
            #TODO
            pass

    @api.depends('state')
    def _compute_color(self):
        self.filtered(lambda match: match.state == 'draft').update({'color': 2})
        self.filtered(lambda match: match.state == 'confirmed').update({'color': 0})
        self.filtered(lambda match: match.state == 'started').update({'color': 6})
        self.filtered(lambda match: match.state == 'done').update({'color': 1})

    def write(self, vals):
        res = super(TournamentMatch, self).write(vals)
        if vals.get('state') == 'confirmed':
            self._check_players()
        elif 'score' in vals:
            self._check_winner()
        return res

    def _check_players(self):
        for match in self:
            if match.first_team_id and not match.second_team_id:
                match.winner_id = match.first_team_id
                match.state = 'done'
                match.prepare_next_match()
            # second shouldn't happen
            # elif match.second_team_id and not match.first_team_id:
            #     match.winner_id = match.second_team_id
            #     match.state = 'done'
            #     match.prepare_next_match()

    def _check_winner(self):
        """ Look at the score and assign a winner if enough sets have been played.

            If a winner is assigned, pass him on to the next round.
            If the match is a final, assign the tournament winner/runner-up.
        """
        for match in self:
            score = json.loads(match.score)
            if score and not (match.first_team_id and match.second_team_id):
                self.write({'score': '[]'})
                raise UserError(_("Both teams need to be defined for a score to be set."))
            team_1_won_sets = team_2_won_sets = 0
            match.winner_id = False
            sets_to_win = match.tournament_id.sets_to_win if match.match_type == 'sets' else 1
            for set_score in score:
                if set_score[0] > set_score[1]:
                    team_1_won_sets += 1
                    if team_1_won_sets == sets_to_win:
                        match.winner_id = match.first_team_id
                elif set_score[0] < set_score[1]:
                    team_2_won_sets += 1
                    if team_2_won_sets == sets_to_win:
                        match.winner_id = match.second_team_id
                else:
                    raise ValidationError(_("Can't have a set with same score for both teams!"))
            if match.winner_id:
                match.state = 'done'
                match.prepare_next_match()
            else:
                match.state = 'started'

    def assign_winner_1(self, team):
        self.ensure_one()
        if self.tournament_id.match_type == 'sets':
            raise UserError(_("Please describe the sets in order to assign a winner"))
        self.score = '[[1,0]]'

    def assign_winner_2(self, team):
        self.ensure_one()
        if self.tournament_id.match_type == 'sets':
            raise UserError(_("Please describe the sets in order to assign a winner"))
        self.score = '[[0,1]]'

    def prepare_next_match(self):
        """ A winner is assigned, he passes on to the next round or, if the match
            was the final, declare the winner and runner-up of the tournament.
        """
        self.ensure_one()
        if not self.next_match_id:
            self.tournament_id.winner_id = self.winner_id
            self.tournament_id.runner_up_id = self.first_team_id.id ^ self.winner_id.id ^ self.second_team_id.id
        else:
            # in the hopes this will respect the order ... (though there is no guarantee on recordset orders)
            if self.next_match_id.previous_match_ids[0].id == self.id:
                self.next_match_id.write({'first_team_id': self.winner_id.id})
            else:
                self.next_match_id.write({'second_team_id': self.winner_id.id})

    def tournament_match_score_action(self):
        # import ipdb; ipdb.set_trace()
        return self.env['ir.actions.act_window'].create({
            "type": "ir.actions.act_window",
            'name': _('Match Score'),
            'res_model': 'tournament.match',
            'view_type': 'form',
            'view_mode': 'form',
            # 'view_id': self.env.ref('tournament.tournament_match_view_form_score').id,
            'res_id': self.id,
            'target': 'current',
            'view_ids': [(5, 0, 0),
                         (0, 0, {'view_mode': 'form', 'view_id': self.env.ref('tournament.tournament_match_view_form_score').id})]
        })
    # <record id="" model="ir.actions.act_window">
    #     <field name="name">Match Score</field>
    #     <field name="res_model">tournament.match</field>
    #     <field name="view_type">form</field>
    #     <field name="view_mode">form</field>
    #     <field name="view_id" ref="tournament_match_view_form_score"/>
    #     <!-- <field name="res_id">active_id</field> -->
    #     <field name="domain">[('id', '=', active_id)]</field>
    #     <field name="target">new</field>
    #     <field name="view_ids" 
    #                eval="[(5, 0, 0),
    #                       (0, 0, {'view_mode': 'form', 'view_id': ref('tournament_match_view_form_score')})]"/>
    # </record>
 