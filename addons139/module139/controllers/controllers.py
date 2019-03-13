# -*- coding: utf-8 -*-
from odoo import http

# class Module139(http.Controller):
#     @http.route('/module139/module139/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module139/module139/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module139.listing', {
#             'root': '/module139/module139',
#             'objects': http.request.env['module139.module139'].search([]),
#         })

#     @http.route('/module139/module139/objects/<model("module139.module139"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module139.object', {
#             'object': obj
#         })