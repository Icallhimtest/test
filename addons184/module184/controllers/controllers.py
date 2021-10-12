# -*- coding: utf-8 -*-
from odoo import http

# class Module184(http.Controller):
#     @http.route('/module184/module184/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module184/module184/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module184.listing', {
#             'root': '/module184/module184',
#             'objects': http.request.env['module184.module184'].search([]),
#         })

#     @http.route('/module184/module184/objects/<model("module184.module184"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module184.object', {
#             'object': obj
#         })