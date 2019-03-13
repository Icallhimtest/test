# -*- coding: utf-8 -*-
from odoo import http

# class Module48(http.Controller):
#     @http.route('/module48/module48/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module48/module48/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module48.listing', {
#             'root': '/module48/module48',
#             'objects': http.request.env['module48.module48'].search([]),
#         })

#     @http.route('/module48/module48/objects/<model("module48.module48"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module48.object', {
#             'object': obj
#         })