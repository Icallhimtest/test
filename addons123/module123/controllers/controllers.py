# -*- coding: utf-8 -*-
from odoo import http

# class Module123(http.Controller):
#     @http.route('/module123/module123/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module123/module123/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module123.listing', {
#             'root': '/module123/module123',
#             'objects': http.request.env['module123.module123'].search([]),
#         })

#     @http.route('/module123/module123/objects/<model("module123.module123"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module123.object', {
#             'object': obj
#         })