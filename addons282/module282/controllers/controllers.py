# -*- coding: utf-8 -*-
from odoo import http

# class Module282(http.Controller):
#     @http.route('/module282/module282/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module282/module282/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module282.listing', {
#             'root': '/module282/module282',
#             'objects': http.request.env['module282.module282'].search([]),
#         })

#     @http.route('/module282/module282/objects/<model("module282.module282"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module282.object', {
#             'object': obj
#         })