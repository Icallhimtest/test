# -*- coding: utf-8 -*-
from odoo import http

# class Module109(http.Controller):
#     @http.route('/module109/module109/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module109/module109/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module109.listing', {
#             'root': '/module109/module109',
#             'objects': http.request.env['module109.module109'].search([]),
#         })

#     @http.route('/module109/module109/objects/<model("module109.module109"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module109.object', {
#             'object': obj
#         })