# -*- coding: utf-8 -*-
from odoo import http

# class Module151(http.Controller):
#     @http.route('/module151/module151/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module151/module151/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module151.listing', {
#             'root': '/module151/module151',
#             'objects': http.request.env['module151.module151'].search([]),
#         })

#     @http.route('/module151/module151/objects/<model("module151.module151"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module151.object', {
#             'object': obj
#         })