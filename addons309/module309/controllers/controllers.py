# -*- coding: utf-8 -*-
from odoo import http

# class Module309(http.Controller):
#     @http.route('/module309/module309/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module309/module309/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module309.listing', {
#             'root': '/module309/module309',
#             'objects': http.request.env['module309.module309'].search([]),
#         })

#     @http.route('/module309/module309/objects/<model("module309.module309"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module309.object', {
#             'object': obj
#         })