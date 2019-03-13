# -*- coding: utf-8 -*-
from odoo import http

# class Module324(http.Controller):
#     @http.route('/module324/module324/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module324/module324/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module324.listing', {
#             'root': '/module324/module324',
#             'objects': http.request.env['module324.module324'].search([]),
#         })

#     @http.route('/module324/module324/objects/<model("module324.module324"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module324.object', {
#             'object': obj
#         })