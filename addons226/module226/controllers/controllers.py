# -*- coding: utf-8 -*-
from odoo import http

# class Module226(http.Controller):
#     @http.route('/module226/module226/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module226/module226/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module226.listing', {
#             'root': '/module226/module226',
#             'objects': http.request.env['module226.module226'].search([]),
#         })

#     @http.route('/module226/module226/objects/<model("module226.module226"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module226.object', {
#             'object': obj
#         })