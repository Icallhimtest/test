# -*- coding: utf-8 -*-
from odoo import http

# class Module312(http.Controller):
#     @http.route('/module312/module312/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module312/module312/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module312.listing', {
#             'root': '/module312/module312',
#             'objects': http.request.env['module312.module312'].search([]),
#         })

#     @http.route('/module312/module312/objects/<model("module312.module312"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module312.object', {
#             'object': obj
#         })