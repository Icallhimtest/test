# -*- coding: utf-8 -*-
from odoo import http

# class Module84(http.Controller):
#     @http.route('/module84/module84/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module84/module84/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module84.listing', {
#             'root': '/module84/module84',
#             'objects': http.request.env['module84.module84'].search([]),
#         })

#     @http.route('/module84/module84/objects/<model("module84.module84"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module84.object', {
#             'object': obj
#         })