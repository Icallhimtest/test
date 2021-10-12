# -*- coding: utf-8 -*-
from odoo import http

# class Module164(http.Controller):
#     @http.route('/module164/module164/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module164/module164/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module164.listing', {
#             'root': '/module164/module164',
#             'objects': http.request.env['module164.module164'].search([]),
#         })

#     @http.route('/module164/module164/objects/<model("module164.module164"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module164.object', {
#             'object': obj
#         })