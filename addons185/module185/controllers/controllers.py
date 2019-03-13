# -*- coding: utf-8 -*-
from odoo import http

# class Module185(http.Controller):
#     @http.route('/module185/module185/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module185/module185/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module185.listing', {
#             'root': '/module185/module185',
#             'objects': http.request.env['module185.module185'].search([]),
#         })

#     @http.route('/module185/module185/objects/<model("module185.module185"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module185.object', {
#             'object': obj
#         })