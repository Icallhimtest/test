# -*- coding: utf-8 -*-
from odoo import http

# class Module146(http.Controller):
#     @http.route('/module146/module146/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module146/module146/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module146.listing', {
#             'root': '/module146/module146',
#             'objects': http.request.env['module146.module146'].search([]),
#         })

#     @http.route('/module146/module146/objects/<model("module146.module146"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module146.object', {
#             'object': obj
#         })