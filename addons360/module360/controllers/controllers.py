# -*- coding: utf-8 -*-
from odoo import http

# class Module360(http.Controller):
#     @http.route('/module360/module360/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module360/module360/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module360.listing', {
#             'root': '/module360/module360',
#             'objects': http.request.env['module360.module360'].search([]),
#         })

#     @http.route('/module360/module360/objects/<model("module360.module360"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module360.object', {
#             'object': obj
#         })