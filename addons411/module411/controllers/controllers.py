# -*- coding: utf-8 -*-
from odoo import http

# class Module411(http.Controller):
#     @http.route('/module411/module411/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module411/module411/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module411.listing', {
#             'root': '/module411/module411',
#             'objects': http.request.env['module411.module411'].search([]),
#         })

#     @http.route('/module411/module411/objects/<model("module411.module411"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module411.object', {
#             'object': obj
#         })