# -*- coding: utf-8 -*-
from odoo import http

# class Module410(http.Controller):
#     @http.route('/module410/module410/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module410/module410/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module410.listing', {
#             'root': '/module410/module410',
#             'objects': http.request.env['module410.module410'].search([]),
#         })

#     @http.route('/module410/module410/objects/<model("module410.module410"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module410.object', {
#             'object': obj
#         })