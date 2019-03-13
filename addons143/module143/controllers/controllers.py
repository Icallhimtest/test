# -*- coding: utf-8 -*-
from odoo import http

# class Module143(http.Controller):
#     @http.route('/module143/module143/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module143/module143/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module143.listing', {
#             'root': '/module143/module143',
#             'objects': http.request.env['module143.module143'].search([]),
#         })

#     @http.route('/module143/module143/objects/<model("module143.module143"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module143.object', {
#             'object': obj
#         })