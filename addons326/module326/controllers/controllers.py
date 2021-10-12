# -*- coding: utf-8 -*-
from odoo import http

# class Module326(http.Controller):
#     @http.route('/module326/module326/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module326/module326/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module326.listing', {
#             'root': '/module326/module326',
#             'objects': http.request.env['module326.module326'].search([]),
#         })

#     @http.route('/module326/module326/objects/<model("module326.module326"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module326.object', {
#             'object': obj
#         })