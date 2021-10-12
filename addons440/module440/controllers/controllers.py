# -*- coding: utf-8 -*-
from odoo import http

# class Module440(http.Controller):
#     @http.route('/module440/module440/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module440/module440/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module440.listing', {
#             'root': '/module440/module440',
#             'objects': http.request.env['module440.module440'].search([]),
#         })

#     @http.route('/module440/module440/objects/<model("module440.module440"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module440.object', {
#             'object': obj
#         })