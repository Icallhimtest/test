# -*- coding: utf-8 -*-
from odoo import http

# class Module232(http.Controller):
#     @http.route('/module232/module232/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module232/module232/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module232.listing', {
#             'root': '/module232/module232',
#             'objects': http.request.env['module232.module232'].search([]),
#         })

#     @http.route('/module232/module232/objects/<model("module232.module232"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module232.object', {
#             'object': obj
#         })