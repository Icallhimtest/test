# -*- coding: utf-8 -*-
from odoo import http

# class Module55(http.Controller):
#     @http.route('/module55/module55/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module55/module55/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module55.listing', {
#             'root': '/module55/module55',
#             'objects': http.request.env['module55.module55'].search([]),
#         })

#     @http.route('/module55/module55/objects/<model("module55.module55"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module55.object', {
#             'object': obj
#         })