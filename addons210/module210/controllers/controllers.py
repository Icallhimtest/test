# -*- coding: utf-8 -*-
from odoo import http

# class Module210(http.Controller):
#     @http.route('/module210/module210/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module210/module210/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module210.listing', {
#             'root': '/module210/module210',
#             'objects': http.request.env['module210.module210'].search([]),
#         })

#     @http.route('/module210/module210/objects/<model("module210.module210"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module210.object', {
#             'object': obj
#         })