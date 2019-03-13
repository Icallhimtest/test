# -*- coding: utf-8 -*-
from odoo import http

# class Module213(http.Controller):
#     @http.route('/module213/module213/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module213/module213/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module213.listing', {
#             'root': '/module213/module213',
#             'objects': http.request.env['module213.module213'].search([]),
#         })

#     @http.route('/module213/module213/objects/<model("module213.module213"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module213.object', {
#             'object': obj
#         })