# -*- coding: utf-8 -*-
from odoo import http

# class Module142(http.Controller):
#     @http.route('/module142/module142/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module142/module142/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module142.listing', {
#             'root': '/module142/module142',
#             'objects': http.request.env['module142.module142'].search([]),
#         })

#     @http.route('/module142/module142/objects/<model("module142.module142"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module142.object', {
#             'object': obj
#         })