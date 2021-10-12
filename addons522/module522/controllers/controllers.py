# -*- coding: utf-8 -*-
from odoo import http

# class Module522(http.Controller):
#     @http.route('/module522/module522/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module522/module522/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module522.listing', {
#             'root': '/module522/module522',
#             'objects': http.request.env['module522.module522'].search([]),
#         })

#     @http.route('/module522/module522/objects/<model("module522.module522"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module522.object', {
#             'object': obj
#         })