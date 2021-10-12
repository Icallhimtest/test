# -*- coding: utf-8 -*-
from odoo import http

# class Module450(http.Controller):
#     @http.route('/module450/module450/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module450/module450/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module450.listing', {
#             'root': '/module450/module450',
#             'objects': http.request.env['module450.module450'].search([]),
#         })

#     @http.route('/module450/module450/objects/<model("module450.module450"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module450.object', {
#             'object': obj
#         })