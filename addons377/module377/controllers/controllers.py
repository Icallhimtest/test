# -*- coding: utf-8 -*-
from odoo import http

# class Module377(http.Controller):
#     @http.route('/module377/module377/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module377/module377/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module377.listing', {
#             'root': '/module377/module377',
#             'objects': http.request.env['module377.module377'].search([]),
#         })

#     @http.route('/module377/module377/objects/<model("module377.module377"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module377.object', {
#             'object': obj
#         })