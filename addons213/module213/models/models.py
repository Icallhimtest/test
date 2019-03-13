# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class module213(models.Model):
#     _name = 'module213.module213'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100