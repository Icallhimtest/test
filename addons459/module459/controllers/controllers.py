# -*- coding: utf-8 -*-
from odoo import http

# class Module459(http.Controller):
#     @http.route('/module459/module459/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module459/module459/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module459.listing', {
#             'root': '/module459/module459',
#             'objects': http.request.env['module459.module459'].search([]),
#         })

#     @http.route('/module459/module459/objects/<model("module459.module459"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module459.object', {
#             'object': obj
#         })