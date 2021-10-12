# -*- coding: utf-8 -*-
from odoo import http

# class Module475(http.Controller):
#     @http.route('/module475/module475/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module475/module475/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module475.listing', {
#             'root': '/module475/module475',
#             'objects': http.request.env['module475.module475'].search([]),
#         })

#     @http.route('/module475/module475/objects/<model("module475.module475"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module475.object', {
#             'object': obj
#         })