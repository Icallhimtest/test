# -*- coding: utf-8 -*-
from odoo import http

# class Module336(http.Controller):
#     @http.route('/module336/module336/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module336/module336/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module336.listing', {
#             'root': '/module336/module336',
#             'objects': http.request.env['module336.module336'].search([]),
#         })

#     @http.route('/module336/module336/objects/<model("module336.module336"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module336.object', {
#             'object': obj
#         })