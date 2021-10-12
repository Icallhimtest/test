# -*- coding: utf-8 -*-
from odoo import http

# class Module467(http.Controller):
#     @http.route('/module467/module467/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module467/module467/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module467.listing', {
#             'root': '/module467/module467',
#             'objects': http.request.env['module467.module467'].search([]),
#         })

#     @http.route('/module467/module467/objects/<model("module467.module467"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module467.object', {
#             'object': obj
#         })