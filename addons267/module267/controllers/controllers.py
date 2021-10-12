# -*- coding: utf-8 -*-
from odoo import http

# class Module267(http.Controller):
#     @http.route('/module267/module267/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module267/module267/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module267.listing', {
#             'root': '/module267/module267',
#             'objects': http.request.env['module267.module267'].search([]),
#         })

#     @http.route('/module267/module267/objects/<model("module267.module267"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module267.object', {
#             'object': obj
#         })