# -*- coding: utf-8 -*-
from odoo import http

# class Module181(http.Controller):
#     @http.route('/module181/module181/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module181/module181/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module181.listing', {
#             'root': '/module181/module181',
#             'objects': http.request.env['module181.module181'].search([]),
#         })

#     @http.route('/module181/module181/objects/<model("module181.module181"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module181.object', {
#             'object': obj
#         })