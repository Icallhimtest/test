# -*- coding: utf-8 -*-
from odoo import http

# class Module297(http.Controller):
#     @http.route('/module297/module297/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module297/module297/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module297.listing', {
#             'root': '/module297/module297',
#             'objects': http.request.env['module297.module297'].search([]),
#         })

#     @http.route('/module297/module297/objects/<model("module297.module297"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module297.object', {
#             'object': obj
#         })