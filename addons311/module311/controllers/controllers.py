# -*- coding: utf-8 -*-
from odoo import http

# class Module311(http.Controller):
#     @http.route('/module311/module311/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module311/module311/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module311.listing', {
#             'root': '/module311/module311',
#             'objects': http.request.env['module311.module311'].search([]),
#         })

#     @http.route('/module311/module311/objects/<model("module311.module311"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module311.object', {
#             'object': obj
#         })