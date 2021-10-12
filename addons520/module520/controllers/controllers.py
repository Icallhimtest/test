# -*- coding: utf-8 -*-
from odoo import http

# class Module520(http.Controller):
#     @http.route('/module520/module520/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module520/module520/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module520.listing', {
#             'root': '/module520/module520',
#             'objects': http.request.env['module520.module520'].search([]),
#         })

#     @http.route('/module520/module520/objects/<model("module520.module520"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module520.object', {
#             'object': obj
#         })