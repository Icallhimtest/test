# -*- coding: utf-8 -*-
from odoo import http

# class Module458(http.Controller):
#     @http.route('/module458/module458/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module458/module458/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module458.listing', {
#             'root': '/module458/module458',
#             'objects': http.request.env['module458.module458'].search([]),
#         })

#     @http.route('/module458/module458/objects/<model("module458.module458"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module458.object', {
#             'object': obj
#         })