# -*- coding: utf-8 -*-
from odoo import http

# class Module279(http.Controller):
#     @http.route('/module279/module279/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module279/module279/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module279.listing', {
#             'root': '/module279/module279',
#             'objects': http.request.env['module279.module279'].search([]),
#         })

#     @http.route('/module279/module279/objects/<model("module279.module279"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module279.object', {
#             'object': obj
#         })