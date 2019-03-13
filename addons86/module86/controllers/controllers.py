# -*- coding: utf-8 -*-
from odoo import http

# class Module86(http.Controller):
#     @http.route('/module86/module86/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module86/module86/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module86.listing', {
#             'root': '/module86/module86',
#             'objects': http.request.env['module86.module86'].search([]),
#         })

#     @http.route('/module86/module86/objects/<model("module86.module86"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module86.object', {
#             'object': obj
#         })