# -*- coding: utf-8 -*-
from odoo import http

# class Module88(http.Controller):
#     @http.route('/module88/module88/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module88/module88/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module88.listing', {
#             'root': '/module88/module88',
#             'objects': http.request.env['module88.module88'].search([]),
#         })

#     @http.route('/module88/module88/objects/<model("module88.module88"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module88.object', {
#             'object': obj
#         })