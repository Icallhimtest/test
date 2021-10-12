# -*- coding: utf-8 -*-
from odoo import http

# class Module38(http.Controller):
#     @http.route('/module38/module38/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module38/module38/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module38.listing', {
#             'root': '/module38/module38',
#             'objects': http.request.env['module38.module38'].search([]),
#         })

#     @http.route('/module38/module38/objects/<model("module38.module38"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module38.object', {
#             'object': obj
#         })