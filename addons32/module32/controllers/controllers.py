# -*- coding: utf-8 -*-
from odoo import http

# class Module32(http.Controller):
#     @http.route('/module32/module32/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module32/module32/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module32.listing', {
#             'root': '/module32/module32',
#             'objects': http.request.env['module32.module32'].search([]),
#         })

#     @http.route('/module32/module32/objects/<model("module32.module32"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module32.object', {
#             'object': obj
#         })