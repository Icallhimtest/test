# -*- coding: utf-8 -*-
from odoo import http

# class Module455(http.Controller):
#     @http.route('/module455/module455/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module455/module455/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module455.listing', {
#             'root': '/module455/module455',
#             'objects': http.request.env['module455.module455'].search([]),
#         })

#     @http.route('/module455/module455/objects/<model("module455.module455"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module455.object', {
#             'object': obj
#         })