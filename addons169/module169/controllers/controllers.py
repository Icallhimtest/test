# -*- coding: utf-8 -*-
from odoo import http

# class Module169(http.Controller):
#     @http.route('/module169/module169/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module169/module169/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module169.listing', {
#             'root': '/module169/module169',
#             'objects': http.request.env['module169.module169'].search([]),
#         })

#     @http.route('/module169/module169/objects/<model("module169.module169"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module169.object', {
#             'object': obj
#         })