# -*- coding: utf-8 -*-
from odoo import http

# class Module140(http.Controller):
#     @http.route('/module140/module140/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module140/module140/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module140.listing', {
#             'root': '/module140/module140',
#             'objects': http.request.env['module140.module140'].search([]),
#         })

#     @http.route('/module140/module140/objects/<model("module140.module140"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module140.object', {
#             'object': obj
#         })