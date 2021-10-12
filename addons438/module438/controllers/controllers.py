# -*- coding: utf-8 -*-
from odoo import http

# class Module438(http.Controller):
#     @http.route('/module438/module438/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module438/module438/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module438.listing', {
#             'root': '/module438/module438',
#             'objects': http.request.env['module438.module438'].search([]),
#         })

#     @http.route('/module438/module438/objects/<model("module438.module438"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module438.object', {
#             'object': obj
#         })