# -*- coding: utf-8 -*-
from odoo import http

# class Module406(http.Controller):
#     @http.route('/module406/module406/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module406/module406/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module406.listing', {
#             'root': '/module406/module406',
#             'objects': http.request.env['module406.module406'].search([]),
#         })

#     @http.route('/module406/module406/objects/<model("module406.module406"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module406.object', {
#             'object': obj
#         })