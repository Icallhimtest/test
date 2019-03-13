# -*- coding: utf-8 -*-
from odoo import http

# class Module316(http.Controller):
#     @http.route('/module316/module316/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module316/module316/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module316.listing', {
#             'root': '/module316/module316',
#             'objects': http.request.env['module316.module316'].search([]),
#         })

#     @http.route('/module316/module316/objects/<model("module316.module316"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module316.object', {
#             'object': obj
#         })