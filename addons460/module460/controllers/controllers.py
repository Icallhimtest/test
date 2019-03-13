# -*- coding: utf-8 -*-
from odoo import http

# class Module460(http.Controller):
#     @http.route('/module460/module460/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module460/module460/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module460.listing', {
#             'root': '/module460/module460',
#             'objects': http.request.env['module460.module460'].search([]),
#         })

#     @http.route('/module460/module460/objects/<model("module460.module460"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module460.object', {
#             'object': obj
#         })