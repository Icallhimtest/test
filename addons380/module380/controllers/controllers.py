# -*- coding: utf-8 -*-
from odoo import http

# class Module380(http.Controller):
#     @http.route('/module380/module380/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module380/module380/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module380.listing', {
#             'root': '/module380/module380',
#             'objects': http.request.env['module380.module380'].search([]),
#         })

#     @http.route('/module380/module380/objects/<model("module380.module380"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module380.object', {
#             'object': obj
#         })