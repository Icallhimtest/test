# -*- coding: utf-8 -*-
from odoo import http

# class Module212(http.Controller):
#     @http.route('/module212/module212/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module212/module212/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module212.listing', {
#             'root': '/module212/module212',
#             'objects': http.request.env['module212.module212'].search([]),
#         })

#     @http.route('/module212/module212/objects/<model("module212.module212"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module212.object', {
#             'object': obj
#         })