# -*- coding: utf-8 -*-
from odoo import http

# class Module133(http.Controller):
#     @http.route('/module133/module133/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module133/module133/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module133.listing', {
#             'root': '/module133/module133',
#             'objects': http.request.env['module133.module133'].search([]),
#         })

#     @http.route('/module133/module133/objects/<model("module133.module133"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module133.object', {
#             'object': obj
#         })