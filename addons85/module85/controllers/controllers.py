# -*- coding: utf-8 -*-
from odoo import http

# class Module85(http.Controller):
#     @http.route('/module85/module85/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module85/module85/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module85.listing', {
#             'root': '/module85/module85',
#             'objects': http.request.env['module85.module85'].search([]),
#         })

#     @http.route('/module85/module85/objects/<model("module85.module85"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module85.object', {
#             'object': obj
#         })