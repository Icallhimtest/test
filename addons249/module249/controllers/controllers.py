# -*- coding: utf-8 -*-
from odoo import http

# class Module249(http.Controller):
#     @http.route('/module249/module249/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module249/module249/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module249.listing', {
#             'root': '/module249/module249',
#             'objects': http.request.env['module249.module249'].search([]),
#         })

#     @http.route('/module249/module249/objects/<model("module249.module249"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module249.object', {
#             'object': obj
#         })