# -*- coding: utf-8 -*-
from odoo import http

# class Module416(http.Controller):
#     @http.route('/module416/module416/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module416/module416/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module416.listing', {
#             'root': '/module416/module416',
#             'objects': http.request.env['module416.module416'].search([]),
#         })

#     @http.route('/module416/module416/objects/<model("module416.module416"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module416.object', {
#             'object': obj
#         })