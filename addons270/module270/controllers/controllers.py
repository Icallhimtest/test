# -*- coding: utf-8 -*-
from odoo import http

# class Module270(http.Controller):
#     @http.route('/module270/module270/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module270/module270/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module270.listing', {
#             'root': '/module270/module270',
#             'objects': http.request.env['module270.module270'].search([]),
#         })

#     @http.route('/module270/module270/objects/<model("module270.module270"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module270.object', {
#             'object': obj
#         })