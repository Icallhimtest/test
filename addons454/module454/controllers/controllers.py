# -*- coding: utf-8 -*-
from odoo import http

# class Module454(http.Controller):
#     @http.route('/module454/module454/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module454/module454/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module454.listing', {
#             'root': '/module454/module454',
#             'objects': http.request.env['module454.module454'].search([]),
#         })

#     @http.route('/module454/module454/objects/<model("module454.module454"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module454.object', {
#             'object': obj
#         })