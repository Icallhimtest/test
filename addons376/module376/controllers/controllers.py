# -*- coding: utf-8 -*-
from odoo import http

# class Module376(http.Controller):
#     @http.route('/module376/module376/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module376/module376/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module376.listing', {
#             'root': '/module376/module376',
#             'objects': http.request.env['module376.module376'].search([]),
#         })

#     @http.route('/module376/module376/objects/<model("module376.module376"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module376.object', {
#             'object': obj
#         })