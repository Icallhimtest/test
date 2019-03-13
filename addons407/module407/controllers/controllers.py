# -*- coding: utf-8 -*-
from odoo import http

# class Module407(http.Controller):
#     @http.route('/module407/module407/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module407/module407/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module407.listing', {
#             'root': '/module407/module407',
#             'objects': http.request.env['module407.module407'].search([]),
#         })

#     @http.route('/module407/module407/objects/<model("module407.module407"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module407.object', {
#             'object': obj
#         })