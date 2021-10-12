# -*- coding: utf-8 -*-
from odoo import http

# class Module303(http.Controller):
#     @http.route('/module303/module303/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module303/module303/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module303.listing', {
#             'root': '/module303/module303',
#             'objects': http.request.env['module303.module303'].search([]),
#         })

#     @http.route('/module303/module303/objects/<model("module303.module303"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module303.object', {
#             'object': obj
#         })