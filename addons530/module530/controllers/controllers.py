# -*- coding: utf-8 -*-
from odoo import http

# class Module530(http.Controller):
#     @http.route('/module530/module530/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module530/module530/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module530.listing', {
#             'root': '/module530/module530',
#             'objects': http.request.env['module530.module530'].search([]),
#         })

#     @http.route('/module530/module530/objects/<model("module530.module530"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module530.object', {
#             'object': obj
#         })