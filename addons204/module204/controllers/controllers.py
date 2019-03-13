# -*- coding: utf-8 -*-
from odoo import http

# class Module204(http.Controller):
#     @http.route('/module204/module204/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module204/module204/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module204.listing', {
#             'root': '/module204/module204',
#             'objects': http.request.env['module204.module204'].search([]),
#         })

#     @http.route('/module204/module204/objects/<model("module204.module204"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module204.object', {
#             'object': obj
#         })