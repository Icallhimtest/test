# -*- coding: utf-8 -*-
from odoo import http

# class Module155(http.Controller):
#     @http.route('/module155/module155/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module155/module155/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module155.listing', {
#             'root': '/module155/module155',
#             'objects': http.request.env['module155.module155'].search([]),
#         })

#     @http.route('/module155/module155/objects/<model("module155.module155"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module155.object', {
#             'object': obj
#         })