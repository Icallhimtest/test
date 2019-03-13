# -*- coding: utf-8 -*-
from odoo import http

# class Module73(http.Controller):
#     @http.route('/module73/module73/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module73/module73/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module73.listing', {
#             'root': '/module73/module73',
#             'objects': http.request.env['module73.module73'].search([]),
#         })

#     @http.route('/module73/module73/objects/<model("module73.module73"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module73.object', {
#             'object': obj
#         })