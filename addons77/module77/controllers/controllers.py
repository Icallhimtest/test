# -*- coding: utf-8 -*-
from odoo import http

# class Module77(http.Controller):
#     @http.route('/module77/module77/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module77/module77/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module77.listing', {
#             'root': '/module77/module77',
#             'objects': http.request.env['module77.module77'].search([]),
#         })

#     @http.route('/module77/module77/objects/<model("module77.module77"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module77.object', {
#             'object': obj
#         })