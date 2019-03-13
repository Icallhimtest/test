# -*- coding: utf-8 -*-
from odoo import http

# class Module334(http.Controller):
#     @http.route('/module334/module334/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module334/module334/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module334.listing', {
#             'root': '/module334/module334',
#             'objects': http.request.env['module334.module334'].search([]),
#         })

#     @http.route('/module334/module334/objects/<model("module334.module334"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module334.object', {
#             'object': obj
#         })