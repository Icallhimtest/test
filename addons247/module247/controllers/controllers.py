# -*- coding: utf-8 -*-
from odoo import http

# class Module247(http.Controller):
#     @http.route('/module247/module247/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module247/module247/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module247.listing', {
#             'root': '/module247/module247',
#             'objects': http.request.env['module247.module247'].search([]),
#         })

#     @http.route('/module247/module247/objects/<model("module247.module247"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module247.object', {
#             'object': obj
#         })