# -*- coding: utf-8 -*-
from odoo import http

# class Module191(http.Controller):
#     @http.route('/module191/module191/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module191/module191/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module191.listing', {
#             'root': '/module191/module191',
#             'objects': http.request.env['module191.module191'].search([]),
#         })

#     @http.route('/module191/module191/objects/<model("module191.module191"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module191.object', {
#             'object': obj
#         })