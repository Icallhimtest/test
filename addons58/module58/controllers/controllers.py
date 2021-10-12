# -*- coding: utf-8 -*-
from odoo import http

# class Module58(http.Controller):
#     @http.route('/module58/module58/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module58/module58/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module58.listing', {
#             'root': '/module58/module58',
#             'objects': http.request.env['module58.module58'].search([]),
#         })

#     @http.route('/module58/module58/objects/<model("module58.module58"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module58.object', {
#             'object': obj
#         })