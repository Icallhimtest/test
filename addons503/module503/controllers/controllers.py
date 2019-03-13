# -*- coding: utf-8 -*-
from odoo import http

# class Module503(http.Controller):
#     @http.route('/module503/module503/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module503/module503/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module503.listing', {
#             'root': '/module503/module503',
#             'objects': http.request.env['module503.module503'].search([]),
#         })

#     @http.route('/module503/module503/objects/<model("module503.module503"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module503.object', {
#             'object': obj
#         })