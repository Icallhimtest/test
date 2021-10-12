# -*- coding: utf-8 -*-
from odoo import http

# class Module206(http.Controller):
#     @http.route('/module206/module206/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module206/module206/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module206.listing', {
#             'root': '/module206/module206',
#             'objects': http.request.env['module206.module206'].search([]),
#         })

#     @http.route('/module206/module206/objects/<model("module206.module206"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module206.object', {
#             'object': obj
#         })