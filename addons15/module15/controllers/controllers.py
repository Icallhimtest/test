# -*- coding: utf-8 -*-
from odoo import http

# class Module15(http.Controller):
#     @http.route('/module15/module15/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module15/module15/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module15.listing', {
#             'root': '/module15/module15',
#             'objects': http.request.env['module15.module15'].search([]),
#         })

#     @http.route('/module15/module15/objects/<model("module15.module15"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module15.object', {
#             'object': obj
#         })