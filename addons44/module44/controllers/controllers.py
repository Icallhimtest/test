# -*- coding: utf-8 -*-
from odoo import http

# class Module44(http.Controller):
#     @http.route('/module44/module44/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module44/module44/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module44.listing', {
#             'root': '/module44/module44',
#             'objects': http.request.env['module44.module44'].search([]),
#         })

#     @http.route('/module44/module44/objects/<model("module44.module44"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module44.object', {
#             'object': obj
#         })