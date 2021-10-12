# -*- coding: utf-8 -*-
from odoo import http

# class Module313(http.Controller):
#     @http.route('/module313/module313/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module313/module313/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module313.listing', {
#             'root': '/module313/module313',
#             'objects': http.request.env['module313.module313'].search([]),
#         })

#     @http.route('/module313/module313/objects/<model("module313.module313"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module313.object', {
#             'object': obj
#         })