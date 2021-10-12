# -*- coding: utf-8 -*-
from odoo import http

# class Module302(http.Controller):
#     @http.route('/module302/module302/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module302/module302/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module302.listing', {
#             'root': '/module302/module302',
#             'objects': http.request.env['module302.module302'].search([]),
#         })

#     @http.route('/module302/module302/objects/<model("module302.module302"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module302.object', {
#             'object': obj
#         })