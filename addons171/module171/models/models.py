# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class module171(models.Model):
#     _name = 'module171.module171'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100