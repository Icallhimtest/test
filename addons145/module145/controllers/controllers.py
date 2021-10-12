# -*- coding: utf-8 -*-
from odoo import http

# class Module145(http.Controller):
#     @http.route('/module145/module145/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module145/module145/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module145.listing', {
#             'root': '/module145/module145',
#             'objects': http.request.env['module145.module145'].search([]),
#         })

#     @http.route('/module145/module145/objects/<model("module145.module145"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module145.object', {
#             'object': obj
#         })