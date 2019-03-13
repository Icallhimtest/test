# -*- coding: utf-8 -*-
from odoo import http

# class Module500(http.Controller):
#     @http.route('/module500/module500/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module500/module500/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module500.listing', {
#             'root': '/module500/module500',
#             'objects': http.request.env['module500.module500'].search([]),
#         })

#     @http.route('/module500/module500/objects/<model("module500.module500"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module500.object', {
#             'object': obj
#         })