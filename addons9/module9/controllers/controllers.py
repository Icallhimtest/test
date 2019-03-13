# -*- coding: utf-8 -*-
from odoo import http

# class Module9(http.Controller):
#     @http.route('/module9/module9/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module9/module9/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module9.listing', {
#             'root': '/module9/module9',
#             'objects': http.request.env['module9.module9'].search([]),
#         })

#     @http.route('/module9/module9/objects/<model("module9.module9"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module9.object', {
#             'object': obj
#         })