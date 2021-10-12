# -*- coding: utf-8 -*-
from odoo import http

# class Module445(http.Controller):
#     @http.route('/module445/module445/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module445/module445/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module445.listing', {
#             'root': '/module445/module445',
#             'objects': http.request.env['module445.module445'].search([]),
#         })

#     @http.route('/module445/module445/objects/<model("module445.module445"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module445.object', {
#             'object': obj
#         })