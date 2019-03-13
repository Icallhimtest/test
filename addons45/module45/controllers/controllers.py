# -*- coding: utf-8 -*-
from odoo import http

# class Module45(http.Controller):
#     @http.route('/module45/module45/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module45/module45/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module45.listing', {
#             'root': '/module45/module45',
#             'objects': http.request.env['module45.module45'].search([]),
#         })

#     @http.route('/module45/module45/objects/<model("module45.module45"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module45.object', {
#             'object': obj
#         })