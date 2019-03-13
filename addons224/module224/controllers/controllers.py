# -*- coding: utf-8 -*-
from odoo import http

# class Module224(http.Controller):
#     @http.route('/module224/module224/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module224/module224/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module224.listing', {
#             'root': '/module224/module224',
#             'objects': http.request.env['module224.module224'].search([]),
#         })

#     @http.route('/module224/module224/objects/<model("module224.module224"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module224.object', {
#             'object': obj
#         })