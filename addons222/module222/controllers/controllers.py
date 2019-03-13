# -*- coding: utf-8 -*-
from odoo import http

# class Module222(http.Controller):
#     @http.route('/module222/module222/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module222/module222/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module222.listing', {
#             'root': '/module222/module222',
#             'objects': http.request.env['module222.module222'].search([]),
#         })

#     @http.route('/module222/module222/objects/<model("module222.module222"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module222.object', {
#             'object': obj
#         })