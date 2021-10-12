# -*- coding: utf-8 -*-
from odoo import http

# class Module331(http.Controller):
#     @http.route('/module331/module331/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module331/module331/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module331.listing', {
#             'root': '/module331/module331',
#             'objects': http.request.env['module331.module331'].search([]),
#         })

#     @http.route('/module331/module331/objects/<model("module331.module331"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module331.object', {
#             'object': obj
#         })