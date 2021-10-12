# -*- coding: utf-8 -*-
from odoo import http

# class Module35(http.Controller):
#     @http.route('/module35/module35/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module35/module35/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module35.listing', {
#             'root': '/module35/module35',
#             'objects': http.request.env['module35.module35'].search([]),
#         })

#     @http.route('/module35/module35/objects/<model("module35.module35"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module35.object', {
#             'object': obj
#         })