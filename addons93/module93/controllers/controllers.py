# -*- coding: utf-8 -*-
from odoo import http

# class Module93(http.Controller):
#     @http.route('/module93/module93/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module93/module93/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module93.listing', {
#             'root': '/module93/module93',
#             'objects': http.request.env['module93.module93'].search([]),
#         })

#     @http.route('/module93/module93/objects/<model("module93.module93"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module93.object', {
#             'object': obj
#         })