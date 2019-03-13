# -*- coding: utf-8 -*-
from odoo import http

# class Module205(http.Controller):
#     @http.route('/module205/module205/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module205/module205/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module205.listing', {
#             'root': '/module205/module205',
#             'objects': http.request.env['module205.module205'].search([]),
#         })

#     @http.route('/module205/module205/objects/<model("module205.module205"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module205.object', {
#             'object': obj
#         })