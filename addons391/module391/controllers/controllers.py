# -*- coding: utf-8 -*-
from odoo import http

# class Module391(http.Controller):
#     @http.route('/module391/module391/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module391/module391/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module391.listing', {
#             'root': '/module391/module391',
#             'objects': http.request.env['module391.module391'].search([]),
#         })

#     @http.route('/module391/module391/objects/<model("module391.module391"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module391.object', {
#             'object': obj
#         })