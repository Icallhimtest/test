# -*- coding: utf-8 -*-
from odoo import http

# class Module175(http.Controller):
#     @http.route('/module175/module175/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module175/module175/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module175.listing', {
#             'root': '/module175/module175',
#             'objects': http.request.env['module175.module175'].search([]),
#         })

#     @http.route('/module175/module175/objects/<model("module175.module175"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module175.object', {
#             'object': obj
#         })