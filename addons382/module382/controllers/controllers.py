# -*- coding: utf-8 -*-
from odoo import http

# class Module382(http.Controller):
#     @http.route('/module382/module382/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module382/module382/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module382.listing', {
#             'root': '/module382/module382',
#             'objects': http.request.env['module382.module382'].search([]),
#         })

#     @http.route('/module382/module382/objects/<model("module382.module382"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module382.object', {
#             'object': obj
#         })