# -*- coding: utf-8 -*-
from odoo import http

# class Module496(http.Controller):
#     @http.route('/module496/module496/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module496/module496/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module496.listing', {
#             'root': '/module496/module496',
#             'objects': http.request.env['module496.module496'].search([]),
#         })

#     @http.route('/module496/module496/objects/<model("module496.module496"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module496.object', {
#             'object': obj
#         })