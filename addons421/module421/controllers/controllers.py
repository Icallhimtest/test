# -*- coding: utf-8 -*-
from odoo import http

# class Module421(http.Controller):
#     @http.route('/module421/module421/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module421/module421/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module421.listing', {
#             'root': '/module421/module421',
#             'objects': http.request.env['module421.module421'].search([]),
#         })

#     @http.route('/module421/module421/objects/<model("module421.module421"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module421.object', {
#             'object': obj
#         })