# -*- coding: utf-8 -*-
from odoo import http

# class Module7(http.Controller):
#     @http.route('/module7/module7/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module7/module7/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module7.listing', {
#             'root': '/module7/module7',
#             'objects': http.request.env['module7.module7'].search([]),
#         })

#     @http.route('/module7/module7/objects/<model("module7.module7"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module7.object', {
#             'object': obj
#         })