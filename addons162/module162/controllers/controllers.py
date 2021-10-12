# -*- coding: utf-8 -*-
from odoo import http

# class Module162(http.Controller):
#     @http.route('/module162/module162/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module162/module162/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module162.listing', {
#             'root': '/module162/module162',
#             'objects': http.request.env['module162.module162'].search([]),
#         })

#     @http.route('/module162/module162/objects/<model("module162.module162"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module162.object', {
#             'object': obj
#         })