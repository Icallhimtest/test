# -*- coding: utf-8 -*-
from odoo import http

# class Module433(http.Controller):
#     @http.route('/module433/module433/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module433/module433/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module433.listing', {
#             'root': '/module433/module433',
#             'objects': http.request.env['module433.module433'].search([]),
#         })

#     @http.route('/module433/module433/objects/<model("module433.module433"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module433.object', {
#             'object': obj
#         })