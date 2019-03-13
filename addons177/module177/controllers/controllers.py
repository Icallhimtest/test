# -*- coding: utf-8 -*-
from odoo import http

# class Module177(http.Controller):
#     @http.route('/module177/module177/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module177/module177/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module177.listing', {
#             'root': '/module177/module177',
#             'objects': http.request.env['module177.module177'].search([]),
#         })

#     @http.route('/module177/module177/objects/<model("module177.module177"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module177.object', {
#             'object': obj
#         })