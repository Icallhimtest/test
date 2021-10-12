# -*- coding: utf-8 -*-
from odoo import http

# class Module201(http.Controller):
#     @http.route('/module201/module201/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module201/module201/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module201.listing', {
#             'root': '/module201/module201',
#             'objects': http.request.env['module201.module201'].search([]),
#         })

#     @http.route('/module201/module201/objects/<model("module201.module201"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module201.object', {
#             'object': obj
#         })