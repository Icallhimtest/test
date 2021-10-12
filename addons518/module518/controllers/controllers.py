# -*- coding: utf-8 -*-
from odoo import http

# class Module518(http.Controller):
#     @http.route('/module518/module518/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module518/module518/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module518.listing', {
#             'root': '/module518/module518',
#             'objects': http.request.env['module518.module518'].search([]),
#         })

#     @http.route('/module518/module518/objects/<model("module518.module518"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module518.object', {
#             'object': obj
#         })