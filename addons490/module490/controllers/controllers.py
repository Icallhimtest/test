# -*- coding: utf-8 -*-
from odoo import http

# class Module490(http.Controller):
#     @http.route('/module490/module490/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module490/module490/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module490.listing', {
#             'root': '/module490/module490',
#             'objects': http.request.env['module490.module490'].search([]),
#         })

#     @http.route('/module490/module490/objects/<model("module490.module490"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module490.object', {
#             'object': obj
#         })