# -*- coding: utf-8 -*-
from odoo import http

# class Module193(http.Controller):
#     @http.route('/module193/module193/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module193/module193/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module193.listing', {
#             'root': '/module193/module193',
#             'objects': http.request.env['module193.module193'].search([]),
#         })

#     @http.route('/module193/module193/objects/<model("module193.module193"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module193.object', {
#             'object': obj
#         })