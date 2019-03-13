# -*- coding: utf-8 -*-
from odoo import http

# class Module251(http.Controller):
#     @http.route('/module251/module251/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module251/module251/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module251.listing', {
#             'root': '/module251/module251',
#             'objects': http.request.env['module251.module251'].search([]),
#         })

#     @http.route('/module251/module251/objects/<model("module251.module251"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module251.object', {
#             'object': obj
#         })