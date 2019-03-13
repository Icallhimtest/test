# -*- coding: utf-8 -*-
from odoo import http

# class Module19(http.Controller):
#     @http.route('/module19/module19/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module19/module19/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module19.listing', {
#             'root': '/module19/module19',
#             'objects': http.request.env['module19.module19'].search([]),
#         })

#     @http.route('/module19/module19/objects/<model("module19.module19"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module19.object', {
#             'object': obj
#         })