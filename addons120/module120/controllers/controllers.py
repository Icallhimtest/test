# -*- coding: utf-8 -*-
from odoo import http

# class Module120(http.Controller):
#     @http.route('/module120/module120/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module120/module120/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module120.listing', {
#             'root': '/module120/module120',
#             'objects': http.request.env['module120.module120'].search([]),
#         })

#     @http.route('/module120/module120/objects/<model("module120.module120"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module120.object', {
#             'object': obj
#         })