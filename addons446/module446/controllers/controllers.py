# -*- coding: utf-8 -*-
from odoo import http

# class Module446(http.Controller):
#     @http.route('/module446/module446/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module446/module446/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module446.listing', {
#             'root': '/module446/module446',
#             'objects': http.request.env['module446.module446'].search([]),
#         })

#     @http.route('/module446/module446/objects/<model("module446.module446"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module446.object', {
#             'object': obj
#         })