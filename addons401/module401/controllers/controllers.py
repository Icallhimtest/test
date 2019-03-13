# -*- coding: utf-8 -*-
from odoo import http

# class Module401(http.Controller):
#     @http.route('/module401/module401/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module401/module401/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module401.listing', {
#             'root': '/module401/module401',
#             'objects': http.request.env['module401.module401'].search([]),
#         })

#     @http.route('/module401/module401/objects/<model("module401.module401"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module401.object', {
#             'object': obj
#         })