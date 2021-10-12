# -*- coding: utf-8 -*-
from odoo import http

# class Module130(http.Controller):
#     @http.route('/module130/module130/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module130/module130/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module130.listing', {
#             'root': '/module130/module130',
#             'objects': http.request.env['module130.module130'].search([]),
#         })

#     @http.route('/module130/module130/objects/<model("module130.module130"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module130.object', {
#             'object': obj
#         })