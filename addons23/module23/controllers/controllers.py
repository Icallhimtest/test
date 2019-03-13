# -*- coding: utf-8 -*-
from odoo import http

# class Module23(http.Controller):
#     @http.route('/module23/module23/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module23/module23/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module23.listing', {
#             'root': '/module23/module23',
#             'objects': http.request.env['module23.module23'].search([]),
#         })

#     @http.route('/module23/module23/objects/<model("module23.module23"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module23.object', {
#             'object': obj
#         })