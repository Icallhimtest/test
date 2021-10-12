# -*- coding: utf-8 -*-
from odoo import http

# class Module52(http.Controller):
#     @http.route('/module52/module52/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module52/module52/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module52.listing', {
#             'root': '/module52/module52',
#             'objects': http.request.env['module52.module52'].search([]),
#         })

#     @http.route('/module52/module52/objects/<model("module52.module52"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module52.object', {
#             'object': obj
#         })