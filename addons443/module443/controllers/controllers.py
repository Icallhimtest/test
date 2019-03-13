# -*- coding: utf-8 -*-
from odoo import http

# class Module443(http.Controller):
#     @http.route('/module443/module443/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module443/module443/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module443.listing', {
#             'root': '/module443/module443',
#             'objects': http.request.env['module443.module443'].search([]),
#         })

#     @http.route('/module443/module443/objects/<model("module443.module443"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module443.object', {
#             'object': obj
#         })