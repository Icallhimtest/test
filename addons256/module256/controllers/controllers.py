# -*- coding: utf-8 -*-
from odoo import http

# class Module256(http.Controller):
#     @http.route('/module256/module256/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module256/module256/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module256.listing', {
#             'root': '/module256/module256',
#             'objects': http.request.env['module256.module256'].search([]),
#         })

#     @http.route('/module256/module256/objects/<model("module256.module256"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module256.object', {
#             'object': obj
#         })