# -*- coding: utf-8 -*-
from odoo import http

# class Module122(http.Controller):
#     @http.route('/module122/module122/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module122/module122/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module122.listing', {
#             'root': '/module122/module122',
#             'objects': http.request.env['module122.module122'].search([]),
#         })

#     @http.route('/module122/module122/objects/<model("module122.module122"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module122.object', {
#             'object': obj
#         })