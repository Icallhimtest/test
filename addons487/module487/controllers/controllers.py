# -*- coding: utf-8 -*-
from odoo import http

# class Module487(http.Controller):
#     @http.route('/module487/module487/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module487/module487/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module487.listing', {
#             'root': '/module487/module487',
#             'objects': http.request.env['module487.module487'].search([]),
#         })

#     @http.route('/module487/module487/objects/<model("module487.module487"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module487.object', {
#             'object': obj
#         })