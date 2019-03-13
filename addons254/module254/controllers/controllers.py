# -*- coding: utf-8 -*-
from odoo import http

# class Module254(http.Controller):
#     @http.route('/module254/module254/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module254/module254/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module254.listing', {
#             'root': '/module254/module254',
#             'objects': http.request.env['module254.module254'].search([]),
#         })

#     @http.route('/module254/module254/objects/<model("module254.module254"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module254.object', {
#             'object': obj
#         })