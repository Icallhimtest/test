# -*- coding: utf-8 -*-
from odoo import http

# class Module463(http.Controller):
#     @http.route('/module463/module463/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module463/module463/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module463.listing', {
#             'root': '/module463/module463',
#             'objects': http.request.env['module463.module463'].search([]),
#         })

#     @http.route('/module463/module463/objects/<model("module463.module463"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module463.object', {
#             'object': obj
#         })