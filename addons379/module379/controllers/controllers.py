# -*- coding: utf-8 -*-
from odoo import http

# class Module379(http.Controller):
#     @http.route('/module379/module379/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module379/module379/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module379.listing', {
#             'root': '/module379/module379',
#             'objects': http.request.env['module379.module379'].search([]),
#         })

#     @http.route('/module379/module379/objects/<model("module379.module379"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module379.object', {
#             'object': obj
#         })