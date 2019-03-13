# -*- coding: utf-8 -*-
from odoo import http

# class Module519(http.Controller):
#     @http.route('/module519/module519/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module519/module519/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module519.listing', {
#             'root': '/module519/module519',
#             'objects': http.request.env['module519.module519'].search([]),
#         })

#     @http.route('/module519/module519/objects/<model("module519.module519"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module519.object', {
#             'object': obj
#         })