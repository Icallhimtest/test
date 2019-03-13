# -*- coding: utf-8 -*-
from odoo import http

# class Module66(http.Controller):
#     @http.route('/module66/module66/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module66/module66/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module66.listing', {
#             'root': '/module66/module66',
#             'objects': http.request.env['module66.module66'].search([]),
#         })

#     @http.route('/module66/module66/objects/<model("module66.module66"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module66.object', {
#             'object': obj
#         })