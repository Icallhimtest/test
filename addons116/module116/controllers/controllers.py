# -*- coding: utf-8 -*-
from odoo import http

# class Module116(http.Controller):
#     @http.route('/module116/module116/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module116/module116/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module116.listing', {
#             'root': '/module116/module116',
#             'objects': http.request.env['module116.module116'].search([]),
#         })

#     @http.route('/module116/module116/objects/<model("module116.module116"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module116.object', {
#             'object': obj
#         })