# -*- coding: utf-8 -*-
from odoo import http

# class Module16(http.Controller):
#     @http.route('/module16/module16/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module16/module16/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module16.listing', {
#             'root': '/module16/module16',
#             'objects': http.request.env['module16.module16'].search([]),
#         })

#     @http.route('/module16/module16/objects/<model("module16.module16"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module16.object', {
#             'object': obj
#         })