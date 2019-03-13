# -*- coding: utf-8 -*-
from odoo import http

# class Module71(http.Controller):
#     @http.route('/module71/module71/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module71/module71/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module71.listing', {
#             'root': '/module71/module71',
#             'objects': http.request.env['module71.module71'].search([]),
#         })

#     @http.route('/module71/module71/objects/<model("module71.module71"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module71.object', {
#             'object': obj
#         })