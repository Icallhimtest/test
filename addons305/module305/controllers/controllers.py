# -*- coding: utf-8 -*-
from odoo import http

# class Module305(http.Controller):
#     @http.route('/module305/module305/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module305/module305/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module305.listing', {
#             'root': '/module305/module305',
#             'objects': http.request.env['module305.module305'].search([]),
#         })

#     @http.route('/module305/module305/objects/<model("module305.module305"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module305.object', {
#             'object': obj
#         })