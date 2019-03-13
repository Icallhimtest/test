# -*- coding: utf-8 -*-
from odoo import http

# class Module106(http.Controller):
#     @http.route('/module106/module106/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module106/module106/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module106.listing', {
#             'root': '/module106/module106',
#             'objects': http.request.env['module106.module106'].search([]),
#         })

#     @http.route('/module106/module106/objects/<model("module106.module106"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module106.object', {
#             'object': obj
#         })