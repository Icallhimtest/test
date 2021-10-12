# -*- coding: utf-8 -*-
from odoo import http

# class Module358(http.Controller):
#     @http.route('/module358/module358/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module358/module358/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module358.listing', {
#             'root': '/module358/module358',
#             'objects': http.request.env['module358.module358'].search([]),
#         })

#     @http.route('/module358/module358/objects/<model("module358.module358"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module358.object', {
#             'object': obj
#         })