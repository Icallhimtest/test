# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import math
import random

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class TournamentTeam(models.Model):
    _name = "tournament.team"

    #TODO is this required ? or does it work automatically?
    def _default_tournament_ids(self):
        if 'default_tournament_id' in self._context:
            return [(4, self._context.get('default_tournament_id'), 0)]

    name = fields.Char(string='Name', compute='_compute_name', store=True)
    player_ids = fields.Many2many('res.partner', string='Players') # TODO: create res.partner inheritance.
    tournament_ids = fields.Many2many('tournament', string='Participated Tournaments', readonly=True, default=_default_tournament_ids)
    next_match_id = fields.Many2one('tournament.match', string='Next match', readonly=True, compute='_compute_next_match_id')
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
                result = "(%s) " % len(team.player_ids)
                for player in team.player_ids:
                    result += player.name.split(' ', 1)[0] + ", "
                team.name = result[:-2]

    def _compute_next_match_id(self):
        for team in self:
            team.next_match_id = self.env['tournament.match'].search(
                domain=['&', ('state', 'in', ('confirmed', 'started')), '|', ('first_team_id', '=', team.id), ('second_team_id', '=', team.id)], limit=1).id

    #name_get method or computed name
