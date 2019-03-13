# -*- coding: utf-8 -*-
from odoo import http

# class Module315(http.Controller):
#     @http.route('/module315/module315/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module315/module315/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module315.listing', {
#             'root': '/module315/module315',
#             'objects': http.request.env['module315.module315'].search([]),
#         })

#     @http.route('/module315/module315/objects/<model("module315.module315"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module315.object', {
#             'object': obj
#         })