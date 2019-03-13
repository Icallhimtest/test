# -*- coding: utf-8 -*-
from odoo import http

# class Module339(http.Controller):
#     @http.route('/module339/module339/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module339/module339/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module339.listing', {
#             'root': '/module339/module339',
#             'objects': http.request.env['module339.module339'].search([]),
#         })

#     @http.route('/module339/module339/objects/<model("module339.module339"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module339.object', {
#             'object': obj
#         })