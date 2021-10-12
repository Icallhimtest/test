# -*- coding: utf-8 -*-
from odoo import http

# class Module178(http.Controller):
#     @http.route('/module178/module178/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module178/module178/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module178.listing', {
#             'root': '/module178/module178',
#             'objects': http.request.env['module178.module178'].search([]),
#         })

#     @http.route('/module178/module178/objects/<model("module178.module178"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module178.object', {
#             'object': obj
#         })