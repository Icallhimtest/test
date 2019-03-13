# -*- coding: utf-8 -*-
from odoo import http

# class Module171(http.Controller):
#     @http.route('/module171/module171/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module171/module171/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module171.listing', {
#             'root': '/module171/module171',
#             'objects': http.request.env['module171.module171'].search([]),
#         })

#     @http.route('/module171/module171/objects/<model("module171.module171"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module171.object', {
#             'object': obj
#         })