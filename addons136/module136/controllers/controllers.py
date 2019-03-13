# -*- coding: utf-8 -*-
from odoo import http

# class Module136(http.Controller):
#     @http.route('/module136/module136/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module136/module136/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module136.listing', {
#             'root': '/module136/module136',
#             'objects': http.request.env['module136.module136'].search([]),
#         })

#     @http.route('/module136/module136/objects/<model("module136.module136"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module136.object', {
#             'object': obj
#         })