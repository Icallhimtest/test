# -*- coding: utf-8 -*-
from odoo import http

# class Module301(http.Controller):
#     @http.route('/module301/module301/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module301/module301/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module301.listing', {
#             'root': '/module301/module301',
#             'objects': http.request.env['module301.module301'].search([]),
#         })

#     @http.route('/module301/module301/objects/<model("module301.module301"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module301.object', {
#             'object': obj
#         })