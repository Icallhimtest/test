# -*- coding: utf-8 -*-
from odoo import http

# class Module425(http.Controller):
#     @http.route('/module425/module425/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module425/module425/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module425.listing', {
#             'root': '/module425/module425',
#             'objects': http.request.env['module425.module425'].search([]),
#         })

#     @http.route('/module425/module425/objects/<model("module425.module425"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module425.object', {
#             'object': obj
#         })