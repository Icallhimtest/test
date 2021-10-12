# -*- coding: utf-8 -*-
from odoo import http

# class Module346(http.Controller):
#     @http.route('/module346/module346/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module346/module346/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module346.listing', {
#             'root': '/module346/module346',
#             'objects': http.request.env['module346.module346'].search([]),
#         })

#     @http.route('/module346/module346/objects/<model("module346.module346"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module346.object', {
#             'object': obj
#         })