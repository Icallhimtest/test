# -*- coding: utf-8 -*-
from odoo import http

# class Module87(http.Controller):
#     @http.route('/module87/module87/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module87/module87/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module87.listing', {
#             'root': '/module87/module87',
#             'objects': http.request.env['module87.module87'].search([]),
#         })

#     @http.route('/module87/module87/objects/<model("module87.module87"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module87.object', {
#             'object': obj
#         })