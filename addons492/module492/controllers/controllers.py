# -*- coding: utf-8 -*-
from odoo import http

# class Module492(http.Controller):
#     @http.route('/module492/module492/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module492/module492/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module492.listing', {
#             'root': '/module492/module492',
#             'objects': http.request.env['module492.module492'].search([]),
#         })

#     @http.route('/module492/module492/objects/<model("module492.module492"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module492.object', {
#             'object': obj
#         })