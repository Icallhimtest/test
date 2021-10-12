# -*- coding: utf-8 -*-
from odoo import http

# class Module21(http.Controller):
#     @http.route('/module21/module21/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module21/module21/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module21.listing', {
#             'root': '/module21/module21',
#             'objects': http.request.env['module21.module21'].search([]),
#         })

#     @http.route('/module21/module21/objects/<model("module21.module21"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module21.object', {
#             'object': obj
#         })