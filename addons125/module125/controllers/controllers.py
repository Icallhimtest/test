# -*- coding: utf-8 -*-
from odoo import http

# class Module125(http.Controller):
#     @http.route('/module125/module125/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module125/module125/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module125.listing', {
#             'root': '/module125/module125',
#             'objects': http.request.env['module125.module125'].search([]),
#         })

#     @http.route('/module125/module125/objects/<model("module125.module125"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module125.object', {
#             'object': obj
#         })