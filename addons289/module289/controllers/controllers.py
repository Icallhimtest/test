# -*- coding: utf-8 -*-
from odoo import http

# class Module289(http.Controller):
#     @http.route('/module289/module289/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module289/module289/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module289.listing', {
#             'root': '/module289/module289',
#             'objects': http.request.env['module289.module289'].search([]),
#         })

#     @http.route('/module289/module289/objects/<model("module289.module289"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module289.object', {
#             'object': obj
#         })