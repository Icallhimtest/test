# -*- coding: utf-8 -*-
from odoo import http

# class Module74(http.Controller):
#     @http.route('/module74/module74/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module74/module74/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module74.listing', {
#             'root': '/module74/module74',
#             'objects': http.request.env['module74.module74'].search([]),
#         })

#     @http.route('/module74/module74/objects/<model("module74.module74"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module74.object', {
#             'object': obj
#         })