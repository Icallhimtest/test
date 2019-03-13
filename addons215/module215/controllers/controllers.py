# -*- coding: utf-8 -*-
from odoo import http

# class Module215(http.Controller):
#     @http.route('/module215/module215/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module215/module215/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module215.listing', {
#             'root': '/module215/module215',
#             'objects': http.request.env['module215.module215'].search([]),
#         })

#     @http.route('/module215/module215/objects/<model("module215.module215"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module215.object', {
#             'object': obj
#         })