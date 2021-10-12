# -*- coding: utf-8 -*-
from odoo import http

# class Module480(http.Controller):
#     @http.route('/module480/module480/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module480/module480/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module480.listing', {
#             'root': '/module480/module480',
#             'objects': http.request.env['module480.module480'].search([]),
#         })

#     @http.route('/module480/module480/objects/<model("module480.module480"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module480.object', {
#             'object': obj
#         })