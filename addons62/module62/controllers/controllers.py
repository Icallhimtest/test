# -*- coding: utf-8 -*-
from odoo import http

# class Module62(http.Controller):
#     @http.route('/module62/module62/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module62/module62/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module62.listing', {
#             'root': '/module62/module62',
#             'objects': http.request.env['module62.module62'].search([]),
#         })

#     @http.route('/module62/module62/objects/<model("module62.module62"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module62.object', {
#             'object': obj
#         })