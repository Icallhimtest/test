# -*- coding: utf-8 -*-
from odoo import http

# class Module14(http.Controller):
#     @http.route('/module14/module14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module14/module14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module14.listing', {
#             'root': '/module14/module14',
#             'objects': http.request.env['module14.module14'].search([]),
#         })

#     @http.route('/module14/module14/objects/<model("module14.module14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module14.object', {
#             'object': obj
#         })