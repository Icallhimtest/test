# -*- coding: utf-8 -*-
from odoo import http

# class Module148(http.Controller):
#     @http.route('/module148/module148/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module148/module148/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module148.listing', {
#             'root': '/module148/module148',
#             'objects': http.request.env['module148.module148'].search([]),
#         })

#     @http.route('/module148/module148/objects/<model("module148.module148"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module148.object', {
#             'object': obj
#         })