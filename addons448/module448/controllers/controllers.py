# -*- coding: utf-8 -*-
from odoo import http

# class Module448(http.Controller):
#     @http.route('/module448/module448/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module448/module448/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module448.listing', {
#             'root': '/module448/module448',
#             'objects': http.request.env['module448.module448'].search([]),
#         })

#     @http.route('/module448/module448/objects/<model("module448.module448"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module448.object', {
#             'object': obj
#         })