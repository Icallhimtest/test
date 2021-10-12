# -*- coding: utf-8 -*-
from odoo import http

# class Module408(http.Controller):
#     @http.route('/module408/module408/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module408/module408/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module408.listing', {
#             'root': '/module408/module408',
#             'objects': http.request.env['module408.module408'].search([]),
#         })

#     @http.route('/module408/module408/objects/<model("module408.module408"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module408.object', {
#             'object': obj
#         })