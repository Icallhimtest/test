# -*- coding: utf-8 -*-
from odoo import http

# class Module257(http.Controller):
#     @http.route('/module257/module257/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module257/module257/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module257.listing', {
#             'root': '/module257/module257',
#             'objects': http.request.env['module257.module257'].search([]),
#         })

#     @http.route('/module257/module257/objects/<model("module257.module257"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module257.object', {
#             'object': obj
#         })