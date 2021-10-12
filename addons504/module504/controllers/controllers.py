# -*- coding: utf-8 -*-
from odoo import http

# class Module504(http.Controller):
#     @http.route('/module504/module504/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module504/module504/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module504.listing', {
#             'root': '/module504/module504',
#             'objects': http.request.env['module504.module504'].search([]),
#         })

#     @http.route('/module504/module504/objects/<model("module504.module504"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module504.object', {
#             'object': obj
#         })