# -*- coding: utf-8 -*-
from odoo import http

# class Module20(http.Controller):
#     @http.route('/module20/module20/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module20/module20/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module20.listing', {
#             'root': '/module20/module20',
#             'objects': http.request.env['module20.module20'].search([]),
#         })

#     @http.route('/module20/module20/objects/<model("module20.module20"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module20.object', {
#             'object': obj
#         })