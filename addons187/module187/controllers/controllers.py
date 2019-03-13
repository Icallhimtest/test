# -*- coding: utf-8 -*-
from odoo import http

# class Module187(http.Controller):
#     @http.route('/module187/module187/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module187/module187/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module187.listing', {
#             'root': '/module187/module187',
#             'objects': http.request.env['module187.module187'].search([]),
#         })

#     @http.route('/module187/module187/objects/<model("module187.module187"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module187.object', {
#             'object': obj
#         })