# -*- coding: utf-8 -*-
from odoo import http

# class Module238(http.Controller):
#     @http.route('/module238/module238/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module238/module238/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module238.listing', {
#             'root': '/module238/module238',
#             'objects': http.request.env['module238.module238'].search([]),
#         })

#     @http.route('/module238/module238/objects/<model("module238.module238"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module238.object', {
#             'object': obj
#         })