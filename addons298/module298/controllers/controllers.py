# -*- coding: utf-8 -*-
from odoo import http

# class Module298(http.Controller):
#     @http.route('/module298/module298/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module298/module298/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module298.listing', {
#             'root': '/module298/module298',
#             'objects': http.request.env['module298.module298'].search([]),
#         })

#     @http.route('/module298/module298/objects/<model("module298.module298"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module298.object', {
#             'object': obj
#         })