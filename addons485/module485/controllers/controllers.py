# -*- coding: utf-8 -*-
from odoo import http

# class Module485(http.Controller):
#     @http.route('/module485/module485/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module485/module485/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module485.listing', {
#             'root': '/module485/module485',
#             'objects': http.request.env['module485.module485'].search([]),
#         })

#     @http.route('/module485/module485/objects/<model("module485.module485"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module485.object', {
#             'object': obj
#         })