# -*- coding: utf-8 -*-
from odoo import http

# class Module274(http.Controller):
#     @http.route('/module274/module274/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module274/module274/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module274.listing', {
#             'root': '/module274/module274',
#             'objects': http.request.env['module274.module274'].search([]),
#         })

#     @http.route('/module274/module274/objects/<model("module274.module274"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module274.object', {
#             'object': obj
#         })