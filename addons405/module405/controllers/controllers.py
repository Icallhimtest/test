# -*- coding: utf-8 -*-
from odoo import http

# class Module405(http.Controller):
#     @http.route('/module405/module405/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module405/module405/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module405.listing', {
#             'root': '/module405/module405',
#             'objects': http.request.env['module405.module405'].search([]),
#         })

#     @http.route('/module405/module405/objects/<model("module405.module405"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module405.object', {
#             'object': obj
#         })