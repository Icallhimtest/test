# -*- coding: utf-8 -*-
from odoo import http

# class Module456(http.Controller):
#     @http.route('/module456/module456/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module456/module456/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module456.listing', {
#             'root': '/module456/module456',
#             'objects': http.request.env['module456.module456'].search([]),
#         })

#     @http.route('/module456/module456/objects/<model("module456.module456"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module456.object', {
#             'object': obj
#         })