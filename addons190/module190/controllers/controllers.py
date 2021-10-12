# -*- coding: utf-8 -*-
from odoo import http

# class Module190(http.Controller):
#     @http.route('/module190/module190/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module190/module190/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module190.listing', {
#             'root': '/module190/module190',
#             'objects': http.request.env['module190.module190'].search([]),
#         })

#     @http.route('/module190/module190/objects/<model("module190.module190"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module190.object', {
#             'object': obj
#         })