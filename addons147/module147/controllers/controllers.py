# -*- coding: utf-8 -*-
from odoo import http

# class Module147(http.Controller):
#     @http.route('/module147/module147/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module147/module147/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module147.listing', {
#             'root': '/module147/module147',
#             'objects': http.request.env['module147.module147'].search([]),
#         })

#     @http.route('/module147/module147/objects/<model("module147.module147"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module147.object', {
#             'object': obj
#         })