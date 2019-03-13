# -*- coding: utf-8 -*-
from odoo import http

# class Module472(http.Controller):
#     @http.route('/module472/module472/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module472/module472/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module472.listing', {
#             'root': '/module472/module472',
#             'objects': http.request.env['module472.module472'].search([]),
#         })

#     @http.route('/module472/module472/objects/<model("module472.module472"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module472.object', {
#             'object': obj
#         })