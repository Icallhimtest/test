# -*- coding: utf-8 -*-
from odoo import http

# class Module195(http.Controller):
#     @http.route('/module195/module195/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module195/module195/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module195.listing', {
#             'root': '/module195/module195',
#             'objects': http.request.env['module195.module195'].search([]),
#         })

#     @http.route('/module195/module195/objects/<model("module195.module195"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module195.object', {
#             'object': obj
#         })