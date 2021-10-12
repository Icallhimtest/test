# -*- coding: utf-8 -*-
from odoo import http

# class Module453(http.Controller):
#     @http.route('/module453/module453/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module453/module453/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module453.listing', {
#             'root': '/module453/module453',
#             'objects': http.request.env['module453.module453'].search([]),
#         })

#     @http.route('/module453/module453/objects/<model("module453.module453"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module453.object', {
#             'object': obj
#         })