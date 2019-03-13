# -*- coding: utf-8 -*-
from odoo import http

# class Module63(http.Controller):
#     @http.route('/module63/module63/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module63/module63/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module63.listing', {
#             'root': '/module63/module63',
#             'objects': http.request.env['module63.module63'].search([]),
#         })

#     @http.route('/module63/module63/objects/<model("module63.module63"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module63.object', {
#             'object': obj
#         })