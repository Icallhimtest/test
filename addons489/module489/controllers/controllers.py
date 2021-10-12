# -*- coding: utf-8 -*-
from odoo import http

# class Module489(http.Controller):
#     @http.route('/module489/module489/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module489/module489/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module489.listing', {
#             'root': '/module489/module489',
#             'objects': http.request.env['module489.module489'].search([]),
#         })

#     @http.route('/module489/module489/objects/<model("module489.module489"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module489.object', {
#             'object': obj
#         })