# -*- coding: utf-8 -*-
from odoo import http

# class Module250(http.Controller):
#     @http.route('/module250/module250/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module250/module250/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module250.listing', {
#             'root': '/module250/module250',
#             'objects': http.request.env['module250.module250'].search([]),
#         })

#     @http.route('/module250/module250/objects/<model("module250.module250"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module250.object', {
#             'object': obj
#         })