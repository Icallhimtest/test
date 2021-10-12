# -*- coding: utf-8 -*-
from odoo import http

# class Module471(http.Controller):
#     @http.route('/module471/module471/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module471/module471/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module471.listing', {
#             'root': '/module471/module471',
#             'objects': http.request.env['module471.module471'].search([]),
#         })

#     @http.route('/module471/module471/objects/<model("module471.module471"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module471.object', {
#             'object': obj
#         })