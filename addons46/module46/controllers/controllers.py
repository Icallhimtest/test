# -*- coding: utf-8 -*-
from odoo import http

# class Module46(http.Controller):
#     @http.route('/module46/module46/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module46/module46/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module46.listing', {
#             'root': '/module46/module46',
#             'objects': http.request.env['module46.module46'].search([]),
#         })

#     @http.route('/module46/module46/objects/<model("module46.module46"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module46.object', {
#             'object': obj
#         })