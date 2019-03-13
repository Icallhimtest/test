# -*- coding: utf-8 -*-
from odoo import http

# class Module330(http.Controller):
#     @http.route('/module330/module330/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module330/module330/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module330.listing', {
#             'root': '/module330/module330',
#             'objects': http.request.env['module330.module330'].search([]),
#         })

#     @http.route('/module330/module330/objects/<model("module330.module330"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module330.object', {
#             'object': obj
#         })