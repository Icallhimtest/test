# -*- coding: utf-8 -*-
from odoo import http

# class Module468(http.Controller):
#     @http.route('/module468/module468/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module468/module468/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module468.listing', {
#             'root': '/module468/module468',
#             'objects': http.request.env['module468.module468'].search([]),
#         })

#     @http.route('/module468/module468/objects/<model("module468.module468"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module468.object', {
#             'object': obj
#         })