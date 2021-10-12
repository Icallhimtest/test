# -*- coding: utf-8 -*-
from odoo import http

# class Module275(http.Controller):
#     @http.route('/module275/module275/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module275/module275/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module275.listing', {
#             'root': '/module275/module275',
#             'objects': http.request.env['module275.module275'].search([]),
#         })

#     @http.route('/module275/module275/objects/<model("module275.module275"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module275.object', {
#             'object': obj
#         })