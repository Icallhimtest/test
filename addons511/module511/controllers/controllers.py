# -*- coding: utf-8 -*-
from odoo import http

# class Module511(http.Controller):
#     @http.route('/module511/module511/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module511/module511/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module511.listing', {
#             'root': '/module511/module511',
#             'objects': http.request.env['module511.module511'].search([]),
#         })

#     @http.route('/module511/module511/objects/<model("module511.module511"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module511.object', {
#             'object': obj
#         })