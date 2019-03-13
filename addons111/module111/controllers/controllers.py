# -*- coding: utf-8 -*-
from odoo import http

# class Module111(http.Controller):
#     @http.route('/module111/module111/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module111/module111/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module111.listing', {
#             'root': '/module111/module111',
#             'objects': http.request.env['module111.module111'].search([]),
#         })

#     @http.route('/module111/module111/objects/<model("module111.module111"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module111.object', {
#             'object': obj
#         })