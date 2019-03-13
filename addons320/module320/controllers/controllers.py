# -*- coding: utf-8 -*-
from odoo import http

# class Module320(http.Controller):
#     @http.route('/module320/module320/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module320/module320/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module320.listing', {
#             'root': '/module320/module320',
#             'objects': http.request.env['module320.module320'].search([]),
#         })

#     @http.route('/module320/module320/objects/<model("module320.module320"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module320.object', {
#             'object': obj
#         })