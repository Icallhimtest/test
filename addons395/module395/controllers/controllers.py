# -*- coding: utf-8 -*-
from odoo import http

# class Module395(http.Controller):
#     @http.route('/module395/module395/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module395/module395/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module395.listing', {
#             'root': '/module395/module395',
#             'objects': http.request.env['module395.module395'].search([]),
#         })

#     @http.route('/module395/module395/objects/<model("module395.module395"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module395.object', {
#             'object': obj
#         })