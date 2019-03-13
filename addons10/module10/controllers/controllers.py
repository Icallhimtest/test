# -*- coding: utf-8 -*-
from odoo import http

# class Module10(http.Controller):
#     @http.route('/module10/module10/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module10/module10/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module10.listing', {
#             'root': '/module10/module10',
#             'objects': http.request.env['module10.module10'].search([]),
#         })

#     @http.route('/module10/module10/objects/<model("module10.module10"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module10.object', {
#             'object': obj
#         })