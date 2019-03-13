# -*- coding: utf-8 -*-
from odoo import http

# class Module137(http.Controller):
#     @http.route('/module137/module137/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module137/module137/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module137.listing', {
#             'root': '/module137/module137',
#             'objects': http.request.env['module137.module137'].search([]),
#         })

#     @http.route('/module137/module137/objects/<model("module137.module137"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module137.object', {
#             'object': obj
#         })