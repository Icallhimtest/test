# -*- coding: utf-8 -*-
from odoo import http

# class Module236(http.Controller):
#     @http.route('/module236/module236/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module236/module236/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module236.listing', {
#             'root': '/module236/module236',
#             'objects': http.request.env['module236.module236'].search([]),
#         })

#     @http.route('/module236/module236/objects/<model("module236.module236"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module236.object', {
#             'object': obj
#         })