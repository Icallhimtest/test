# -*- coding: utf-8 -*-
from odoo import http

# class Module259(http.Controller):
#     @http.route('/module259/module259/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module259/module259/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module259.listing', {
#             'root': '/module259/module259',
#             'objects': http.request.env['module259.module259'].search([]),
#         })

#     @http.route('/module259/module259/objects/<model("module259.module259"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module259.object', {
#             'object': obj
#         })