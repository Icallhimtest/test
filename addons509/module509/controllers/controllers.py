# -*- coding: utf-8 -*-
from odoo import http

# class Module509(http.Controller):
#     @http.route('/module509/module509/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module509/module509/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module509.listing', {
#             'root': '/module509/module509',
#             'objects': http.request.env['module509.module509'].search([]),
#         })

#     @http.route('/module509/module509/objects/<model("module509.module509"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module509.object', {
#             'object': obj
#         })