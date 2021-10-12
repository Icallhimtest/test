# -*- coding: utf-8 -*-
from odoo import http

# class Module83(http.Controller):
#     @http.route('/module83/module83/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module83/module83/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module83.listing', {
#             'root': '/module83/module83',
#             'objects': http.request.env['module83.module83'].search([]),
#         })

#     @http.route('/module83/module83/objects/<model("module83.module83"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module83.object', {
#             'object': obj
#         })