# -*- coding: utf-8 -*-
from odoo import http

# class Module117(http.Controller):
#     @http.route('/module117/module117/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module117/module117/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module117.listing', {
#             'root': '/module117/module117',
#             'objects': http.request.env['module117.module117'].search([]),
#         })

#     @http.route('/module117/module117/objects/<model("module117.module117"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module117.object', {
#             'object': obj
#         })