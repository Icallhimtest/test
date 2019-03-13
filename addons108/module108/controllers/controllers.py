# -*- coding: utf-8 -*-
from odoo import http

# class Module108(http.Controller):
#     @http.route('/module108/module108/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module108/module108/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module108.listing', {
#             'root': '/module108/module108',
#             'objects': http.request.env['module108.module108'].search([]),
#         })

#     @http.route('/module108/module108/objects/<model("module108.module108"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module108.object', {
#             'object': obj
#         })