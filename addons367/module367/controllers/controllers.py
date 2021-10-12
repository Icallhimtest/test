# -*- coding: utf-8 -*-
from odoo import http

# class Module367(http.Controller):
#     @http.route('/module367/module367/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module367/module367/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module367.listing', {
#             'root': '/module367/module367',
#             'objects': http.request.env['module367.module367'].search([]),
#         })

#     @http.route('/module367/module367/objects/<model("module367.module367"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module367.object', {
#             'object': obj
#         })