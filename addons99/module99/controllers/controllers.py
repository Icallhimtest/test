# -*- coding: utf-8 -*-
from odoo import http

# class Module99(http.Controller):
#     @http.route('/module99/module99/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module99/module99/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module99.listing', {
#             'root': '/module99/module99',
#             'objects': http.request.env['module99.module99'].search([]),
#         })

#     @http.route('/module99/module99/objects/<model("module99.module99"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module99.object', {
#             'object': obj
#         })