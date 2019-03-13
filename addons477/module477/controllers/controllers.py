# -*- coding: utf-8 -*-
from odoo import http

# class Module477(http.Controller):
#     @http.route('/module477/module477/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module477/module477/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module477.listing', {
#             'root': '/module477/module477',
#             'objects': http.request.env['module477.module477'].search([]),
#         })

#     @http.route('/module477/module477/objects/<model("module477.module477"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module477.object', {
#             'object': obj
#         })