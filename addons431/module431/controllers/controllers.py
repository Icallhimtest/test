# -*- coding: utf-8 -*-
from odoo import http

# class Module431(http.Controller):
#     @http.route('/module431/module431/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module431/module431/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module431.listing', {
#             'root': '/module431/module431',
#             'objects': http.request.env['module431.module431'].search([]),
#         })

#     @http.route('/module431/module431/objects/<model("module431.module431"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module431.object', {
#             'object': obj
#         })