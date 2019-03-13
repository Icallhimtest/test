# -*- coding: utf-8 -*-
from odoo import http

# class Module12(http.Controller):
#     @http.route('/module12/module12/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module12/module12/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module12.listing', {
#             'root': '/module12/module12',
#             'objects': http.request.env['module12.module12'].search([]),
#         })

#     @http.route('/module12/module12/objects/<model("module12.module12"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module12.object', {
#             'object': obj
#         })