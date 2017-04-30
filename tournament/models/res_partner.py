# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import math
import random

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class Partner(models.Model):
    _inherit = 'res.partner'

    team_ids = fields.Many2many('tournament.team', string='Tournament Teams', readonly=True)
    is_player = fields.Boolean('Participates in Tournaments')
    gender = fields.Selection([
    	('male', 'Man'),
    	('female', 'Woman'),
    ])
