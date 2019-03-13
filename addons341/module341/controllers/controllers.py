# -*- coding: utf-8 -*-
from odoo import http

# class Module341(http.Controller):
#     @http.route('/module341/module341/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module341/module341/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module341.listing', {
#             'root': '/module341/module341',
#             'objects': http.request.env['module341.module341'].search([]),
#         })

#     @http.route('/module341/module341/objects/<model("module341.module341"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module341.object', {
#             'object': obj
#         })