# -*- coding: utf-8 -*-
from odoo import http

# class Module403(http.Controller):
#     @http.route('/module403/module403/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module403/module403/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module403.listing', {
#             'root': '/module403/module403',
#             'objects': http.request.env['module403.module403'].search([]),
#         })

#     @http.route('/module403/module403/objects/<model("module403.module403"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module403.object', {
#             'object': obj
#         })