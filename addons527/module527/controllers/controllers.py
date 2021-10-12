# -*- coding: utf-8 -*-
from odoo import http

# class Module527(http.Controller):
#     @http.route('/module527/module527/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module527/module527/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module527.listing', {
#             'root': '/module527/module527',
#             'objects': http.request.env['module527.module527'].search([]),
#         })

#     @http.route('/module527/module527/objects/<model("module527.module527"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module527.object', {
#             'object': obj
#         })