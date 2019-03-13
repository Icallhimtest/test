# -*- coding: utf-8 -*-
from odoo import http

# class Module69(http.Controller):
#     @http.route('/module69/module69/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module69/module69/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module69.listing', {
#             'root': '/module69/module69',
#             'objects': http.request.env['module69.module69'].search([]),
#         })

#     @http.route('/module69/module69/objects/<model("module69.module69"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module69.object', {
#             'object': obj
#         })