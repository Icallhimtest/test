# -*- coding: utf-8 -*-
from odoo import http

# class Module420(http.Controller):
#     @http.route('/module420/module420/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module420/module420/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module420.listing', {
#             'root': '/module420/module420',
#             'objects': http.request.env['module420.module420'].search([]),
#         })

#     @http.route('/module420/module420/objects/<model("module420.module420"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module420.object', {
#             'object': obj
#         })