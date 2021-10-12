# -*- coding: utf-8 -*-
from odoo import http

# class Module75(http.Controller):
#     @http.route('/module75/module75/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module75/module75/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module75.listing', {
#             'root': '/module75/module75',
#             'objects': http.request.env['module75.module75'].search([]),
#         })

#     @http.route('/module75/module75/objects/<model("module75.module75"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module75.object', {
#             'object': obj
#         })