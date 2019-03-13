# -*- coding: utf-8 -*-
from odoo import http

# class Module507(http.Controller):
#     @http.route('/module507/module507/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module507/module507/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module507.listing', {
#             'root': '/module507/module507',
#             'objects': http.request.env['module507.module507'].search([]),
#         })

#     @http.route('/module507/module507/objects/<model("module507.module507"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module507.object', {
#             'object': obj
#         })