# -*- coding: utf-8 -*-
from odoo import http

# class Module299(http.Controller):
#     @http.route('/module299/module299/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module299/module299/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module299.listing', {
#             'root': '/module299/module299',
#             'objects': http.request.env['module299.module299'].search([]),
#         })

#     @http.route('/module299/module299/objects/<model("module299.module299"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module299.object', {
#             'object': obj
#         })