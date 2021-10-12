# -*- coding: utf-8 -*-
from odoo import http

# class Module36(http.Controller):
#     @http.route('/module36/module36/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module36/module36/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module36.listing', {
#             'root': '/module36/module36',
#             'objects': http.request.env['module36.module36'].search([]),
#         })

#     @http.route('/module36/module36/objects/<model("module36.module36"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module36.object', {
#             'object': obj
#         })