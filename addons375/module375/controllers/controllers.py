# -*- coding: utf-8 -*-
from odoo import http

# class Module375(http.Controller):
#     @http.route('/module375/module375/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module375/module375/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module375.listing', {
#             'root': '/module375/module375',
#             'objects': http.request.env['module375.module375'].search([]),
#         })

#     @http.route('/module375/module375/objects/<model("module375.module375"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module375.object', {
#             'object': obj
#         })