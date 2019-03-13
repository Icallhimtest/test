# -*- coding: utf-8 -*-
from odoo import http

# class Module24(http.Controller):
#     @http.route('/module24/module24/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module24/module24/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module24.listing', {
#             'root': '/module24/module24',
#             'objects': http.request.env['module24.module24'].search([]),
#         })

#     @http.route('/module24/module24/objects/<model("module24.module24"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module24.object', {
#             'object': obj
#         })