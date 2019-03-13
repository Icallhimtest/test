# -*- coding: utf-8 -*-
from odoo import http

# class Module242(http.Controller):
#     @http.route('/module242/module242/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module242/module242/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module242.listing', {
#             'root': '/module242/module242',
#             'objects': http.request.env['module242.module242'].search([]),
#         })

#     @http.route('/module242/module242/objects/<model("module242.module242"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module242.object', {
#             'object': obj
#         })