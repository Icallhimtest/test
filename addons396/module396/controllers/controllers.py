# -*- coding: utf-8 -*-
from odoo import http

# class Module396(http.Controller):
#     @http.route('/module396/module396/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module396/module396/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module396.listing', {
#             'root': '/module396/module396',
#             'objects': http.request.env['module396.module396'].search([]),
#         })

#     @http.route('/module396/module396/objects/<model("module396.module396"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module396.object', {
#             'object': obj
#         })