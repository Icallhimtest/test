# -*- coding: utf-8 -*-
from odoo import http

# class Module402(http.Controller):
#     @http.route('/module402/module402/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module402/module402/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module402.listing', {
#             'root': '/module402/module402',
#             'objects': http.request.env['module402.module402'].search([]),
#         })

#     @http.route('/module402/module402/objects/<model("module402.module402"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module402.object', {
#             'object': obj
#         })