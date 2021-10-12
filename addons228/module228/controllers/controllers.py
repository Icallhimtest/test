# -*- coding: utf-8 -*-
from odoo import http

# class Module228(http.Controller):
#     @http.route('/module228/module228/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module228/module228/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module228.listing', {
#             'root': '/module228/module228',
#             'objects': http.request.env['module228.module228'].search([]),
#         })

#     @http.route('/module228/module228/objects/<model("module228.module228"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module228.object', {
#             'object': obj
#         })