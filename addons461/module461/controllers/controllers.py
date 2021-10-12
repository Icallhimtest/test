# -*- coding: utf-8 -*-
from odoo import http

# class Module461(http.Controller):
#     @http.route('/module461/module461/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module461/module461/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module461.listing', {
#             'root': '/module461/module461',
#             'objects': http.request.env['module461.module461'].search([]),
#         })

#     @http.route('/module461/module461/objects/<model("module461.module461"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module461.object', {
#             'object': obj
#         })