# -*- coding: utf-8 -*-
from odoo import http

# class Module25(http.Controller):
#     @http.route('/module25/module25/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module25/module25/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module25.listing', {
#             'root': '/module25/module25',
#             'objects': http.request.env['module25.module25'].search([]),
#         })

#     @http.route('/module25/module25/objects/<model("module25.module25"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module25.object', {
#             'object': obj
#         })