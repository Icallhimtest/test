# -*- coding: utf-8 -*-
from odoo import http

# class Module328(http.Controller):
#     @http.route('/module328/module328/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module328/module328/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module328.listing', {
#             'root': '/module328/module328',
#             'objects': http.request.env['module328.module328'].search([]),
#         })

#     @http.route('/module328/module328/objects/<model("module328.module328"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module328.object', {
#             'object': obj
#         })