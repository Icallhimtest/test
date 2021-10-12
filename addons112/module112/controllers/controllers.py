# -*- coding: utf-8 -*-
from odoo import http

# class Module112(http.Controller):
#     @http.route('/module112/module112/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module112/module112/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module112.listing', {
#             'root': '/module112/module112',
#             'objects': http.request.env['module112.module112'].search([]),
#         })

#     @http.route('/module112/module112/objects/<model("module112.module112"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module112.object', {
#             'object': obj
#         })