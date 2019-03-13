# -*- coding: utf-8 -*-
from odoo import http

# class Module370(http.Controller):
#     @http.route('/module370/module370/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module370/module370/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module370.listing', {
#             'root': '/module370/module370',
#             'objects': http.request.env['module370.module370'].search([]),
#         })

#     @http.route('/module370/module370/objects/<model("module370.module370"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module370.object', {
#             'object': obj
#         })