# -*- coding: utf-8 -*-
from odoo import http

# class Module192(http.Controller):
#     @http.route('/module192/module192/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module192/module192/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module192.listing', {
#             'root': '/module192/module192',
#             'objects': http.request.env['module192.module192'].search([]),
#         })

#     @http.route('/module192/module192/objects/<model("module192.module192"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module192.object', {
#             'object': obj
#         })