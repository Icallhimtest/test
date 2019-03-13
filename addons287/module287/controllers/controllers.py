# -*- coding: utf-8 -*-
from odoo import http

# class Module287(http.Controller):
#     @http.route('/module287/module287/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module287/module287/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module287.listing', {
#             'root': '/module287/module287',
#             'objects': http.request.env['module287.module287'].search([]),
#         })

#     @http.route('/module287/module287/objects/<model("module287.module287"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module287.object', {
#             'object': obj
#         })