# -*- coding: utf-8 -*-
from odoo import http

# class Module13(http.Controller):
#     @http.route('/module13/module13/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module13/module13/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module13.listing', {
#             'root': '/module13/module13',
#             'objects': http.request.env['module13.module13'].search([]),
#         })

#     @http.route('/module13/module13/objects/<model("module13.module13"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module13.object', {
#             'object': obj
#         })