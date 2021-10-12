# -*- coding: utf-8 -*-
from odoo import http

# class Module156(http.Controller):
#     @http.route('/module156/module156/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module156/module156/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module156.listing', {
#             'root': '/module156/module156',
#             'objects': http.request.env['module156.module156'].search([]),
#         })

#     @http.route('/module156/module156/objects/<model("module156.module156"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module156.object', {
#             'object': obj
#         })