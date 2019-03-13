# -*- coding: utf-8 -*-
from odoo import http

# class Module60(http.Controller):
#     @http.route('/module60/module60/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module60/module60/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module60.listing', {
#             'root': '/module60/module60',
#             'objects': http.request.env['module60.module60'].search([]),
#         })

#     @http.route('/module60/module60/objects/<model("module60.module60"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module60.object', {
#             'object': obj
#         })