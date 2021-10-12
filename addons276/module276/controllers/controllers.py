# -*- coding: utf-8 -*-
from odoo import http

# class Module276(http.Controller):
#     @http.route('/module276/module276/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module276/module276/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module276.listing', {
#             'root': '/module276/module276',
#             'objects': http.request.env['module276.module276'].search([]),
#         })

#     @http.route('/module276/module276/objects/<model("module276.module276"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module276.object', {
#             'object': obj
#         })