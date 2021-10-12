# -*- coding: utf-8 -*-
from odoo import http

# class Module333(http.Controller):
#     @http.route('/module333/module333/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module333/module333/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module333.listing', {
#             'root': '/module333/module333',
#             'objects': http.request.env['module333.module333'].search([]),
#         })

#     @http.route('/module333/module333/objects/<model("module333.module333"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module333.object', {
#             'object': obj
#         })