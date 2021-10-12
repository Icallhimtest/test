# -*- coding: utf-8 -*-
from odoo import http

# class Module457(http.Controller):
#     @http.route('/module457/module457/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module457/module457/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module457.listing', {
#             'root': '/module457/module457',
#             'objects': http.request.env['module457.module457'].search([]),
#         })

#     @http.route('/module457/module457/objects/<model("module457.module457"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module457.object', {
#             'object': obj
#         })