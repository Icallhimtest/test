# -*- coding: utf-8 -*-
from odoo import http

# class Module513(http.Controller):
#     @http.route('/module513/module513/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module513/module513/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module513.listing', {
#             'root': '/module513/module513',
#             'objects': http.request.env['module513.module513'].search([]),
#         })

#     @http.route('/module513/module513/objects/<model("module513.module513"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module513.object', {
#             'object': obj
#         })