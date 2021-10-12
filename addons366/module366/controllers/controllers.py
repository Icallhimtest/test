# -*- coding: utf-8 -*-
from odoo import http

# class Module366(http.Controller):
#     @http.route('/module366/module366/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module366/module366/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module366.listing', {
#             'root': '/module366/module366',
#             'objects': http.request.env['module366.module366'].search([]),
#         })

#     @http.route('/module366/module366/objects/<model("module366.module366"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module366.object', {
#             'object': obj
#         })