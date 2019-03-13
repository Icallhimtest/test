# -*- coding: utf-8 -*-
from odoo import http

# class Module27(http.Controller):
#     @http.route('/module27/module27/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module27/module27/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module27.listing', {
#             'root': '/module27/module27',
#             'objects': http.request.env['module27.module27'].search([]),
#         })

#     @http.route('/module27/module27/objects/<model("module27.module27"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module27.object', {
#             'object': obj
#         })