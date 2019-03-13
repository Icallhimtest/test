# -*- coding: utf-8 -*-
from odoo import http

# class Module470(http.Controller):
#     @http.route('/module470/module470/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module470/module470/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module470.listing', {
#             'root': '/module470/module470',
#             'objects': http.request.env['module470.module470'].search([]),
#         })

#     @http.route('/module470/module470/objects/<model("module470.module470"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module470.object', {
#             'object': obj
#         })