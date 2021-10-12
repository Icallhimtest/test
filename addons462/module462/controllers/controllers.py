# -*- coding: utf-8 -*-
from odoo import http

# class Module462(http.Controller):
#     @http.route('/module462/module462/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module462/module462/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module462.listing', {
#             'root': '/module462/module462',
#             'objects': http.request.env['module462.module462'].search([]),
#         })

#     @http.route('/module462/module462/objects/<model("module462.module462"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module462.object', {
#             'object': obj
#         })