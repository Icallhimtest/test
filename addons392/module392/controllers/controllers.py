# -*- coding: utf-8 -*-
from odoo import http

# class Module392(http.Controller):
#     @http.route('/module392/module392/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module392/module392/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module392.listing', {
#             'root': '/module392/module392',
#             'objects': http.request.env['module392.module392'].search([]),
#         })

#     @http.route('/module392/module392/objects/<model("module392.module392"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module392.object', {
#             'object': obj
#         })