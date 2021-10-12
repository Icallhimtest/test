# -*- coding: utf-8 -*-
from odoo import http

# class Module219(http.Controller):
#     @http.route('/module219/module219/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module219/module219/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module219.listing', {
#             'root': '/module219/module219',
#             'objects': http.request.env['module219.module219'].search([]),
#         })

#     @http.route('/module219/module219/objects/<model("module219.module219"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module219.object', {
#             'object': obj
#         })