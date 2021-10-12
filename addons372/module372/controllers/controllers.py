# -*- coding: utf-8 -*-
from odoo import http

# class Module372(http.Controller):
#     @http.route('/module372/module372/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module372/module372/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module372.listing', {
#             'root': '/module372/module372',
#             'objects': http.request.env['module372.module372'].search([]),
#         })

#     @http.route('/module372/module372/objects/<model("module372.module372"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module372.object', {
#             'object': obj
#         })