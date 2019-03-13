# -*- coding: utf-8 -*-
from odoo import http

# class Module523(http.Controller):
#     @http.route('/module523/module523/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module523/module523/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module523.listing', {
#             'root': '/module523/module523',
#             'objects': http.request.env['module523.module523'].search([]),
#         })

#     @http.route('/module523/module523/objects/<model("module523.module523"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module523.object', {
#             'object': obj
#         })