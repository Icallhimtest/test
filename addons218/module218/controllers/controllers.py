# -*- coding: utf-8 -*-
from odoo import http

# class Module218(http.Controller):
#     @http.route('/module218/module218/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module218/module218/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module218.listing', {
#             'root': '/module218/module218',
#             'objects': http.request.env['module218.module218'].search([]),
#         })

#     @http.route('/module218/module218/objects/<model("module218.module218"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module218.object', {
#             'object': obj
#         })