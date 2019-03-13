# -*- coding: utf-8 -*-
from odoo import http

# class Module239(http.Controller):
#     @http.route('/module239/module239/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module239/module239/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module239.listing', {
#             'root': '/module239/module239',
#             'objects': http.request.env['module239.module239'].search([]),
#         })

#     @http.route('/module239/module239/objects/<model("module239.module239"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module239.object', {
#             'object': obj
#         })