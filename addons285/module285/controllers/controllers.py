# -*- coding: utf-8 -*-
from odoo import http

# class Module285(http.Controller):
#     @http.route('/module285/module285/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module285/module285/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module285.listing', {
#             'root': '/module285/module285',
#             'objects': http.request.env['module285.module285'].search([]),
#         })

#     @http.route('/module285/module285/objects/<model("module285.module285"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module285.object', {
#             'object': obj
#         })