# -*- coding: utf-8 -*-
from odoo import http

# class Module95(http.Controller):
#     @http.route('/module95/module95/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module95/module95/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module95.listing', {
#             'root': '/module95/module95',
#             'objects': http.request.env['module95.module95'].search([]),
#         })

#     @http.route('/module95/module95/objects/<model("module95.module95"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module95.object', {
#             'object': obj
#         })