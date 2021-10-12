# -*- coding: utf-8 -*-
from odoo import http

# class Module295(http.Controller):
#     @http.route('/module295/module295/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module295/module295/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module295.listing', {
#             'root': '/module295/module295',
#             'objects': http.request.env['module295.module295'].search([]),
#         })

#     @http.route('/module295/module295/objects/<model("module295.module295"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module295.object', {
#             'object': obj
#         })