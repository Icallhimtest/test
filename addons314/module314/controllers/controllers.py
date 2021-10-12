# -*- coding: utf-8 -*-
from odoo import http

# class Module314(http.Controller):
#     @http.route('/module314/module314/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module314/module314/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module314.listing', {
#             'root': '/module314/module314',
#             'objects': http.request.env['module314.module314'].search([]),
#         })

#     @http.route('/module314/module314/objects/<model("module314.module314"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module314.object', {
#             'object': obj
#         })