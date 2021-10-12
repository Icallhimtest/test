# -*- coding: utf-8 -*-
from odoo import http

# class Module29(http.Controller):
#     @http.route('/module29/module29/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module29/module29/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module29.listing', {
#             'root': '/module29/module29',
#             'objects': http.request.env['module29.module29'].search([]),
#         })

#     @http.route('/module29/module29/objects/<model("module29.module29"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module29.object', {
#             'object': obj
#         })