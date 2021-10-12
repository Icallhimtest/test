# -*- coding: utf-8 -*-
from odoo import http

# class Module502(http.Controller):
#     @http.route('/module502/module502/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module502/module502/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module502.listing', {
#             'root': '/module502/module502',
#             'objects': http.request.env['module502.module502'].search([]),
#         })

#     @http.route('/module502/module502/objects/<model("module502.module502"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module502.object', {
#             'object': obj
#         })