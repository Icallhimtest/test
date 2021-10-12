# -*- coding: utf-8 -*-
from odoo import http

# class Module469(http.Controller):
#     @http.route('/module469/module469/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module469/module469/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module469.listing', {
#             'root': '/module469/module469',
#             'objects': http.request.env['module469.module469'].search([]),
#         })

#     @http.route('/module469/module469/objects/<model("module469.module469"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module469.object', {
#             'object': obj
#         })