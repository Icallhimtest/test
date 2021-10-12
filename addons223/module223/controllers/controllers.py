# -*- coding: utf-8 -*-
from odoo import http

# class Module223(http.Controller):
#     @http.route('/module223/module223/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module223/module223/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module223.listing', {
#             'root': '/module223/module223',
#             'objects': http.request.env['module223.module223'].search([]),
#         })

#     @http.route('/module223/module223/objects/<model("module223.module223"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module223.object', {
#             'object': obj
#         })