# -*- coding: utf-8 -*-
from odoo import http

# class Module466(http.Controller):
#     @http.route('/module466/module466/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module466/module466/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module466.listing', {
#             'root': '/module466/module466',
#             'objects': http.request.env['module466.module466'].search([]),
#         })

#     @http.route('/module466/module466/objects/<model("module466.module466"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module466.object', {
#             'object': obj
#         })