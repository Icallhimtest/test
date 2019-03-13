# -*- coding: utf-8 -*-
from odoo import http

# class Module149(http.Controller):
#     @http.route('/module149/module149/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module149/module149/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module149.listing', {
#             'root': '/module149/module149',
#             'objects': http.request.env['module149.module149'].search([]),
#         })

#     @http.route('/module149/module149/objects/<model("module149.module149"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module149.object', {
#             'object': obj
#         })