# -*- coding: utf-8 -*-
from odoo import http

# class Module196(http.Controller):
#     @http.route('/module196/module196/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module196/module196/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module196.listing', {
#             'root': '/module196/module196',
#             'objects': http.request.env['module196.module196'].search([]),
#         })

#     @http.route('/module196/module196/objects/<model("module196.module196"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module196.object', {
#             'object': obj
#         })