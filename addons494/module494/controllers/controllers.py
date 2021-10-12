# -*- coding: utf-8 -*-
from odoo import http

# class Module494(http.Controller):
#     @http.route('/module494/module494/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module494/module494/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module494.listing', {
#             'root': '/module494/module494',
#             'objects': http.request.env['module494.module494'].search([]),
#         })

#     @http.route('/module494/module494/objects/<model("module494.module494"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module494.object', {
#             'object': obj
#         })