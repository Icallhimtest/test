# -*- coding: utf-8 -*-
from odoo import http

# class Module437(http.Controller):
#     @http.route('/module437/module437/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module437/module437/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module437.listing', {
#             'root': '/module437/module437',
#             'objects': http.request.env['module437.module437'].search([]),
#         })

#     @http.route('/module437/module437/objects/<model("module437.module437"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module437.object', {
#             'object': obj
#         })