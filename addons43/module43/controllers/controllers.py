# -*- coding: utf-8 -*-
from odoo import http

# class Module43(http.Controller):
#     @http.route('/module43/module43/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module43/module43/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module43.listing', {
#             'root': '/module43/module43',
#             'objects': http.request.env['module43.module43'].search([]),
#         })

#     @http.route('/module43/module43/objects/<model("module43.module43"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module43.object', {
#             'object': obj
#         })