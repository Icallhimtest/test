# -*- coding: utf-8 -*-
from odoo import http

# class Module272(http.Controller):
#     @http.route('/module272/module272/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module272/module272/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module272.listing', {
#             'root': '/module272/module272',
#             'objects': http.request.env['module272.module272'].search([]),
#         })

#     @http.route('/module272/module272/objects/<model("module272.module272"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module272.object', {
#             'object': obj
#         })