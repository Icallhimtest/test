# -*- coding: utf-8 -*-
from odoo import http

# class Module89(http.Controller):
#     @http.route('/module89/module89/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module89/module89/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module89.listing', {
#             'root': '/module89/module89',
#             'objects': http.request.env['module89.module89'].search([]),
#         })

#     @http.route('/module89/module89/objects/<model("module89.module89"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module89.object', {
#             'object': obj
#         })