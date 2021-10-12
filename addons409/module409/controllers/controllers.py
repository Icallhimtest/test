# -*- coding: utf-8 -*-
from odoo import http

# class Module409(http.Controller):
#     @http.route('/module409/module409/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module409/module409/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module409.listing', {
#             'root': '/module409/module409',
#             'objects': http.request.env['module409.module409'].search([]),
#         })

#     @http.route('/module409/module409/objects/<model("module409.module409"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module409.object', {
#             'object': obj
#         })