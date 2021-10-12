# -*- coding: utf-8 -*-
from odoo import http

# class Module418(http.Controller):
#     @http.route('/module418/module418/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module418/module418/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module418.listing', {
#             'root': '/module418/module418',
#             'objects': http.request.env['module418.module418'].search([]),
#         })

#     @http.route('/module418/module418/objects/<model("module418.module418"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module418.object', {
#             'object': obj
#         })