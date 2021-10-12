# -*- coding: utf-8 -*-
from odoo import http

# class Module505(http.Controller):
#     @http.route('/module505/module505/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module505/module505/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module505.listing', {
#             'root': '/module505/module505',
#             'objects': http.request.env['module505.module505'].search([]),
#         })

#     @http.route('/module505/module505/objects/<model("module505.module505"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module505.object', {
#             'object': obj
#         })