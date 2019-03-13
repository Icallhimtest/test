# -*- coding: utf-8 -*-
from odoo import http

# class Module345(http.Controller):
#     @http.route('/module345/module345/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module345/module345/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module345.listing', {
#             'root': '/module345/module345',
#             'objects': http.request.env['module345.module345'].search([]),
#         })

#     @http.route('/module345/module345/objects/<model("module345.module345"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module345.object', {
#             'object': obj
#         })