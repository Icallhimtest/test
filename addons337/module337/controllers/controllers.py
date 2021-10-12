# -*- coding: utf-8 -*-
from odoo import http

# class Module337(http.Controller):
#     @http.route('/module337/module337/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module337/module337/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module337.listing', {
#             'root': '/module337/module337',
#             'objects': http.request.env['module337.module337'].search([]),
#         })

#     @http.route('/module337/module337/objects/<model("module337.module337"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module337.object', {
#             'object': obj
#         })