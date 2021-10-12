# -*- coding: utf-8 -*-
from odoo import http

# class Module415(http.Controller):
#     @http.route('/module415/module415/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module415/module415/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module415.listing', {
#             'root': '/module415/module415',
#             'objects': http.request.env['module415.module415'].search([]),
#         })

#     @http.route('/module415/module415/objects/<model("module415.module415"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module415.object', {
#             'object': obj
#         })