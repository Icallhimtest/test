# -*- coding: utf-8 -*-
from odoo import http

# class Module255(http.Controller):
#     @http.route('/module255/module255/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module255/module255/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module255.listing', {
#             'root': '/module255/module255',
#             'objects': http.request.env['module255.module255'].search([]),
#         })

#     @http.route('/module255/module255/objects/<model("module255.module255"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module255.object', {
#             'object': obj
#         })