# -*- coding: utf-8 -*-
from odoo import http

# class Module474(http.Controller):
#     @http.route('/module474/module474/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module474/module474/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module474.listing', {
#             'root': '/module474/module474',
#             'objects': http.request.env['module474.module474'].search([]),
#         })

#     @http.route('/module474/module474/objects/<model("module474.module474"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module474.object', {
#             'object': obj
#         })