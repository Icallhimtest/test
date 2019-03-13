# -*- coding: utf-8 -*-
from odoo import http

# class Module221(http.Controller):
#     @http.route('/module221/module221/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module221/module221/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module221.listing', {
#             'root': '/module221/module221',
#             'objects': http.request.env['module221.module221'].search([]),
#         })

#     @http.route('/module221/module221/objects/<model("module221.module221"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module221.object', {
#             'object': obj
#         })