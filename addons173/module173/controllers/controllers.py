# -*- coding: utf-8 -*-
from odoo import http

# class Module173(http.Controller):
#     @http.route('/module173/module173/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module173/module173/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module173.listing', {
#             'root': '/module173/module173',
#             'objects': http.request.env['module173.module173'].search([]),
#         })

#     @http.route('/module173/module173/objects/<model("module173.module173"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module173.object', {
#             'object': obj
#         })