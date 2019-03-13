# -*- coding: utf-8 -*-
from odoo import http

# class Module383(http.Controller):
#     @http.route('/module383/module383/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module383/module383/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module383.listing', {
#             'root': '/module383/module383',
#             'objects': http.request.env['module383.module383'].search([]),
#         })

#     @http.route('/module383/module383/objects/<model("module383.module383"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module383.object', {
#             'object': obj
#         })