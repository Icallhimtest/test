# -*- coding: utf-8 -*-
from odoo import http

# class Module158(http.Controller):
#     @http.route('/module158/module158/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module158/module158/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module158.listing', {
#             'root': '/module158/module158',
#             'objects': http.request.env['module158.module158'].search([]),
#         })

#     @http.route('/module158/module158/objects/<model("module158.module158"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module158.object', {
#             'object': obj
#         })