# -*- coding: utf-8 -*-
from odoo import http

# class Module364(http.Controller):
#     @http.route('/module364/module364/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module364/module364/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module364.listing', {
#             'root': '/module364/module364',
#             'objects': http.request.env['module364.module364'].search([]),
#         })

#     @http.route('/module364/module364/objects/<model("module364.module364"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module364.object', {
#             'object': obj
#         })