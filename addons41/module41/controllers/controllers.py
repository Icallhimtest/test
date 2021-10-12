# -*- coding: utf-8 -*-
from odoo import http

# class Module41(http.Controller):
#     @http.route('/module41/module41/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module41/module41/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module41.listing', {
#             'root': '/module41/module41',
#             'objects': http.request.env['module41.module41'].search([]),
#         })

#     @http.route('/module41/module41/objects/<model("module41.module41"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module41.object', {
#             'object': obj
#         })