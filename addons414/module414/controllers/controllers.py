# -*- coding: utf-8 -*-
from odoo import http

# class Module414(http.Controller):
#     @http.route('/module414/module414/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module414/module414/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module414.listing', {
#             'root': '/module414/module414',
#             'objects': http.request.env['module414.module414'].search([]),
#         })

#     @http.route('/module414/module414/objects/<model("module414.module414"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module414.object', {
#             'object': obj
#         })