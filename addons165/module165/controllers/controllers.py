# -*- coding: utf-8 -*-
from odoo import http

# class Module165(http.Controller):
#     @http.route('/module165/module165/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module165/module165/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module165.listing', {
#             'root': '/module165/module165',
#             'objects': http.request.env['module165.module165'].search([]),
#         })

#     @http.route('/module165/module165/objects/<model("module165.module165"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module165.object', {
#             'object': obj
#         })