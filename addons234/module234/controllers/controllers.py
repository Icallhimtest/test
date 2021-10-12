# -*- coding: utf-8 -*-
from odoo import http

# class Module234(http.Controller):
#     @http.route('/module234/module234/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module234/module234/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module234.listing', {
#             'root': '/module234/module234',
#             'objects': http.request.env['module234.module234'].search([]),
#         })

#     @http.route('/module234/module234/objects/<model("module234.module234"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module234.object', {
#             'object': obj
#         })