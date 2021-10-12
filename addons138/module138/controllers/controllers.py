# -*- coding: utf-8 -*-
from odoo import http

# class Module138(http.Controller):
#     @http.route('/module138/module138/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module138/module138/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module138.listing', {
#             'root': '/module138/module138',
#             'objects': http.request.env['module138.module138'].search([]),
#         })

#     @http.route('/module138/module138/objects/<model("module138.module138"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module138.object', {
#             'object': obj
#         })