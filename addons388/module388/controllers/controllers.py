# -*- coding: utf-8 -*-
from odoo import http

# class Module388(http.Controller):
#     @http.route('/module388/module388/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module388/module388/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module388.listing', {
#             'root': '/module388/module388',
#             'objects': http.request.env['module388.module388'].search([]),
#         })

#     @http.route('/module388/module388/objects/<model("module388.module388"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module388.object', {
#             'object': obj
#         })