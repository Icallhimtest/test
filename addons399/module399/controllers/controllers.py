# -*- coding: utf-8 -*-
from odoo import http

# class Module399(http.Controller):
#     @http.route('/module399/module399/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module399/module399/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module399.listing', {
#             'root': '/module399/module399',
#             'objects': http.request.env['module399.module399'].search([]),
#         })

#     @http.route('/module399/module399/objects/<model("module399.module399"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module399.object', {
#             'object': obj
#         })