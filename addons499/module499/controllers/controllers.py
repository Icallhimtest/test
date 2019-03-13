# -*- coding: utf-8 -*-
from odoo import http

# class Module499(http.Controller):
#     @http.route('/module499/module499/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module499/module499/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module499.listing', {
#             'root': '/module499/module499',
#             'objects': http.request.env['module499.module499'].search([]),
#         })

#     @http.route('/module499/module499/objects/<model("module499.module499"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module499.object', {
#             'object': obj
#         })