# -*- coding: utf-8 -*-
from odoo import http

# class Module349(http.Controller):
#     @http.route('/module349/module349/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module349/module349/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module349.listing', {
#             'root': '/module349/module349',
#             'objects': http.request.env['module349.module349'].search([]),
#         })

#     @http.route('/module349/module349/objects/<model("module349.module349"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module349.object', {
#             'object': obj
#         })