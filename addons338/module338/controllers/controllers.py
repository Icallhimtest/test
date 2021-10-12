# -*- coding: utf-8 -*-
from odoo import http

# class Module338(http.Controller):
#     @http.route('/module338/module338/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module338/module338/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module338.listing', {
#             'root': '/module338/module338',
#             'objects': http.request.env['module338.module338'].search([]),
#         })

#     @http.route('/module338/module338/objects/<model("module338.module338"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module338.object', {
#             'object': obj
#         })