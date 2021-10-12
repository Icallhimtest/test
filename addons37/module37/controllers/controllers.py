# -*- coding: utf-8 -*-
from odoo import http

# class Module37(http.Controller):
#     @http.route('/module37/module37/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module37/module37/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module37.listing', {
#             'root': '/module37/module37',
#             'objects': http.request.env['module37.module37'].search([]),
#         })

#     @http.route('/module37/module37/objects/<model("module37.module37"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module37.object', {
#             'object': obj
#         })