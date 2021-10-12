# -*- coding: utf-8 -*-
from odoo import http

# class Module422(http.Controller):
#     @http.route('/module422/module422/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module422/module422/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module422.listing', {
#             'root': '/module422/module422',
#             'objects': http.request.env['module422.module422'].search([]),
#         })

#     @http.route('/module422/module422/objects/<model("module422.module422"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module422.object', {
#             'object': obj
#         })