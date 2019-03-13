# -*- coding: utf-8 -*-
from odoo import http

# class Module56(http.Controller):
#     @http.route('/module56/module56/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module56/module56/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module56.listing', {
#             'root': '/module56/module56',
#             'objects': http.request.env['module56.module56'].search([]),
#         })

#     @http.route('/module56/module56/objects/<model("module56.module56"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module56.object', {
#             'object': obj
#         })