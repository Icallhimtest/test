# -*- coding: utf-8 -*-
from odoo import http

# class Module355(http.Controller):
#     @http.route('/module355/module355/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module355/module355/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module355.listing', {
#             'root': '/module355/module355',
#             'objects': http.request.env['module355.module355'].search([]),
#         })

#     @http.route('/module355/module355/objects/<model("module355.module355"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module355.object', {
#             'object': obj
#         })