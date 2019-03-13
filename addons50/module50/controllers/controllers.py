# -*- coding: utf-8 -*-
from odoo import http

# class Module50(http.Controller):
#     @http.route('/module50/module50/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module50/module50/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module50.listing', {
#             'root': '/module50/module50',
#             'objects': http.request.env['module50.module50'].search([]),
#         })

#     @http.route('/module50/module50/objects/<model("module50.module50"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module50.object', {
#             'object': obj
#         })