# -*- coding: utf-8 -*-
from odoo import http

# class Module92(http.Controller):
#     @http.route('/module92/module92/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module92/module92/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module92.listing', {
#             'root': '/module92/module92',
#             'objects': http.request.env['module92.module92'].search([]),
#         })

#     @http.route('/module92/module92/objects/<model("module92.module92"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module92.object', {
#             'object': obj
#         })