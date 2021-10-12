# -*- coding: utf-8 -*-
from odoo import http

# class Module174(http.Controller):
#     @http.route('/module174/module174/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module174/module174/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module174.listing', {
#             'root': '/module174/module174',
#             'objects': http.request.env['module174.module174'].search([]),
#         })

#     @http.route('/module174/module174/objects/<model("module174.module174"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module174.object', {
#             'object': obj
#         })