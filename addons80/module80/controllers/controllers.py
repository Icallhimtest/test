# -*- coding: utf-8 -*-
from odoo import http

# class Module80(http.Controller):
#     @http.route('/module80/module80/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module80/module80/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module80.listing', {
#             'root': '/module80/module80',
#             'objects': http.request.env['module80.module80'].search([]),
#         })

#     @http.route('/module80/module80/objects/<model("module80.module80"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module80.object', {
#             'object': obj
#         })