# -*- coding: utf-8 -*-
from odoo import http

# class Module114(http.Controller):
#     @http.route('/module114/module114/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module114/module114/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module114.listing', {
#             'root': '/module114/module114',
#             'objects': http.request.env['module114.module114'].search([]),
#         })

#     @http.route('/module114/module114/objects/<model("module114.module114"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module114.object', {
#             'object': obj
#         })