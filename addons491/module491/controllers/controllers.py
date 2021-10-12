# -*- coding: utf-8 -*-
from odoo import http

# class Module491(http.Controller):
#     @http.route('/module491/module491/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module491/module491/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module491.listing', {
#             'root': '/module491/module491',
#             'objects': http.request.env['module491.module491'].search([]),
#         })

#     @http.route('/module491/module491/objects/<model("module491.module491"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module491.object', {
#             'object': obj
#         })