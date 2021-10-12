# -*- coding: utf-8 -*-
from odoo import http

# class Module387(http.Controller):
#     @http.route('/module387/module387/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module387/module387/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module387.listing', {
#             'root': '/module387/module387',
#             'objects': http.request.env['module387.module387'].search([]),
#         })

#     @http.route('/module387/module387/objects/<model("module387.module387"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module387.object', {
#             'object': obj
#         })