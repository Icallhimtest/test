# -*- coding: utf-8 -*-
from odoo import http

# class Module246(http.Controller):
#     @http.route('/module246/module246/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module246/module246/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module246.listing', {
#             'root': '/module246/module246',
#             'objects': http.request.env['module246.module246'].search([]),
#         })

#     @http.route('/module246/module246/objects/<model("module246.module246"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module246.object', {
#             'object': obj
#         })