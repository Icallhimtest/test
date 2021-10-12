# -*- coding: utf-8 -*-
from odoo import http

# class Module197(http.Controller):
#     @http.route('/module197/module197/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module197/module197/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module197.listing', {
#             'root': '/module197/module197',
#             'objects': http.request.env['module197.module197'].search([]),
#         })

#     @http.route('/module197/module197/objects/<model("module197.module197"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module197.object', {
#             'object': obj
#         })