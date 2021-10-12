# -*- coding: utf-8 -*-
from odoo import http

# class Module67(http.Controller):
#     @http.route('/module67/module67/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module67/module67/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module67.listing', {
#             'root': '/module67/module67',
#             'objects': http.request.env['module67.module67'].search([]),
#         })

#     @http.route('/module67/module67/objects/<model("module67.module67"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module67.object', {
#             'object': obj
#         })