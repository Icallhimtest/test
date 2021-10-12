# -*- coding: utf-8 -*-
from odoo import http

# class Module269(http.Controller):
#     @http.route('/module269/module269/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module269/module269/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module269.listing', {
#             'root': '/module269/module269',
#             'objects': http.request.env['module269.module269'].search([]),
#         })

#     @http.route('/module269/module269/objects/<model("module269.module269"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module269.object', {
#             'object': obj
#         })