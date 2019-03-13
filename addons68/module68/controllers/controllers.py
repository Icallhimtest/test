# -*- coding: utf-8 -*-
from odoo import http

# class Module68(http.Controller):
#     @http.route('/module68/module68/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module68/module68/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module68.listing', {
#             'root': '/module68/module68',
#             'objects': http.request.env['module68.module68'].search([]),
#         })

#     @http.route('/module68/module68/objects/<model("module68.module68"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module68.object', {
#             'object': obj
#         })