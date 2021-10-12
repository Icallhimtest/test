# -*- coding: utf-8 -*-
from odoo import http

# class Module154(http.Controller):
#     @http.route('/module154/module154/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module154/module154/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module154.listing', {
#             'root': '/module154/module154',
#             'objects': http.request.env['module154.module154'].search([]),
#         })

#     @http.route('/module154/module154/objects/<model("module154.module154"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module154.object', {
#             'object': obj
#         })