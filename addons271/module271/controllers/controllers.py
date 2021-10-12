# -*- coding: utf-8 -*-
from odoo import http

# class Module271(http.Controller):
#     @http.route('/module271/module271/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module271/module271/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module271.listing', {
#             'root': '/module271/module271',
#             'objects': http.request.env['module271.module271'].search([]),
#         })

#     @http.route('/module271/module271/objects/<model("module271.module271"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module271.object', {
#             'object': obj
#         })