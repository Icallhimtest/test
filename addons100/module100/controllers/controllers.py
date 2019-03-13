# -*- coding: utf-8 -*-
from odoo import http

# class Module100(http.Controller):
#     @http.route('/module100/module100/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module100/module100/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module100.listing', {
#             'root': '/module100/module100',
#             'objects': http.request.env['module100.module100'].search([]),
#         })

#     @http.route('/module100/module100/objects/<model("module100.module100"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module100.object', {
#             'object': obj
#         })