# -*- coding: utf-8 -*-
from odoo import http

# class Module524(http.Controller):
#     @http.route('/module524/module524/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module524/module524/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module524.listing', {
#             'root': '/module524/module524',
#             'objects': http.request.env['module524.module524'].search([]),
#         })

#     @http.route('/module524/module524/objects/<model("module524.module524"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module524.object', {
#             'object': obj
#         })