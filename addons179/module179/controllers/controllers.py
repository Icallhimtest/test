# -*- coding: utf-8 -*-
from odoo import http

# class Module179(http.Controller):
#     @http.route('/module179/module179/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module179/module179/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module179.listing', {
#             'root': '/module179/module179',
#             'objects': http.request.env['module179.module179'].search([]),
#         })

#     @http.route('/module179/module179/objects/<model("module179.module179"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module179.object', {
#             'object': obj
#         })