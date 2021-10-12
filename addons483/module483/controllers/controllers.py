# -*- coding: utf-8 -*-
from odoo import http

# class Module483(http.Controller):
#     @http.route('/module483/module483/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module483/module483/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module483.listing', {
#             'root': '/module483/module483',
#             'objects': http.request.env['module483.module483'].search([]),
#         })

#     @http.route('/module483/module483/objects/<model("module483.module483"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module483.object', {
#             'object': obj
#         })