# -*- coding: utf-8 -*-
from odoo import http

# class Module59(http.Controller):
#     @http.route('/module59/module59/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module59/module59/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module59.listing', {
#             'root': '/module59/module59',
#             'objects': http.request.env['module59.module59'].search([]),
#         })

#     @http.route('/module59/module59/objects/<model("module59.module59"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module59.object', {
#             'object': obj
#         })