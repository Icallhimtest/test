# -*- coding: utf-8 -*-
from odoo import http

# class Module260(http.Controller):
#     @http.route('/module260/module260/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module260/module260/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module260.listing', {
#             'root': '/module260/module260',
#             'objects': http.request.env['module260.module260'].search([]),
#         })

#     @http.route('/module260/module260/objects/<model("module260.module260"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module260.object', {
#             'object': obj
#         })