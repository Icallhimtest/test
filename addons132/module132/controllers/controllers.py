# -*- coding: utf-8 -*-
from odoo import http

# class Module132(http.Controller):
#     @http.route('/module132/module132/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module132/module132/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module132.listing', {
#             'root': '/module132/module132',
#             'objects': http.request.env['module132.module132'].search([]),
#         })

#     @http.route('/module132/module132/objects/<model("module132.module132"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module132.object', {
#             'object': obj
#         })