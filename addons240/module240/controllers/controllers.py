# -*- coding: utf-8 -*-
from odoo import http

# class Module240(http.Controller):
#     @http.route('/module240/module240/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module240/module240/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module240.listing', {
#             'root': '/module240/module240',
#             'objects': http.request.env['module240.module240'].search([]),
#         })

#     @http.route('/module240/module240/objects/<model("module240.module240"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module240.object', {
#             'object': obj
#         })