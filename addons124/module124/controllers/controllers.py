# -*- coding: utf-8 -*-
from odoo import http

# class Module124(http.Controller):
#     @http.route('/module124/module124/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module124/module124/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module124.listing', {
#             'root': '/module124/module124',
#             'objects': http.request.env['module124.module124'].search([]),
#         })

#     @http.route('/module124/module124/objects/<model("module124.module124"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module124.object', {
#             'object': obj
#         })