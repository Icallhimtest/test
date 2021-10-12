# -*- coding: utf-8 -*-
from odoo import http

# class Module72(http.Controller):
#     @http.route('/module72/module72/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module72/module72/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module72.listing', {
#             'root': '/module72/module72',
#             'objects': http.request.env['module72.module72'].search([]),
#         })

#     @http.route('/module72/module72/objects/<model("module72.module72"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module72.object', {
#             'object': obj
#         })