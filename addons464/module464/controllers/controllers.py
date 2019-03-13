# -*- coding: utf-8 -*-
from odoo import http

# class Module464(http.Controller):
#     @http.route('/module464/module464/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module464/module464/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module464.listing', {
#             'root': '/module464/module464',
#             'objects': http.request.env['module464.module464'].search([]),
#         })

#     @http.route('/module464/module464/objects/<model("module464.module464"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module464.object', {
#             'object': obj
#         })