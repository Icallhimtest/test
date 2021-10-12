# -*- coding: utf-8 -*-
from odoo import http

# class Module225(http.Controller):
#     @http.route('/module225/module225/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module225/module225/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module225.listing', {
#             'root': '/module225/module225',
#             'objects': http.request.env['module225.module225'].search([]),
#         })

#     @http.route('/module225/module225/objects/<model("module225.module225"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module225.object', {
#             'object': obj
#         })