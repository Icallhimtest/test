# -*- coding: utf-8 -*-
from odoo import http

# class Module188(http.Controller):
#     @http.route('/module188/module188/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module188/module188/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module188.listing', {
#             'root': '/module188/module188',
#             'objects': http.request.env['module188.module188'].search([]),
#         })

#     @http.route('/module188/module188/objects/<model("module188.module188"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module188.object', {
#             'object': obj
#         })