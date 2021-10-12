# -*- coding: utf-8 -*-
from odoo import http

# class Module22(http.Controller):
#     @http.route('/module22/module22/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module22/module22/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module22.listing', {
#             'root': '/module22/module22',
#             'objects': http.request.env['module22.module22'].search([]),
#         })

#     @http.route('/module22/module22/objects/<model("module22.module22"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module22.object', {
#             'object': obj
#         })