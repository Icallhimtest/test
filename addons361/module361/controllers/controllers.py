# -*- coding: utf-8 -*-
from odoo import http

# class Module361(http.Controller):
#     @http.route('/module361/module361/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module361/module361/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module361.listing', {
#             'root': '/module361/module361',
#             'objects': http.request.env['module361.module361'].search([]),
#         })

#     @http.route('/module361/module361/objects/<model("module361.module361"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module361.object', {
#             'object': obj
#         })