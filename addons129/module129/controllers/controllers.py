# -*- coding: utf-8 -*-
from odoo import http

# class Module129(http.Controller):
#     @http.route('/module129/module129/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module129/module129/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module129.listing', {
#             'root': '/module129/module129',
#             'objects': http.request.env['module129.module129'].search([]),
#         })

#     @http.route('/module129/module129/objects/<model("module129.module129"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module129.object', {
#             'object': obj
#         })