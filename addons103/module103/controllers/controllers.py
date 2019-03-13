# -*- coding: utf-8 -*-
from odoo import http

# class Module103(http.Controller):
#     @http.route('/module103/module103/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module103/module103/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module103.listing', {
#             'root': '/module103/module103',
#             'objects': http.request.env['module103.module103'].search([]),
#         })

#     @http.route('/module103/module103/objects/<model("module103.module103"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module103.object', {
#             'object': obj
#         })