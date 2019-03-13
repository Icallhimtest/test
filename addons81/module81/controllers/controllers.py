# -*- coding: utf-8 -*-
from odoo import http

# class Module81(http.Controller):
#     @http.route('/module81/module81/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module81/module81/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module81.listing', {
#             'root': '/module81/module81',
#             'objects': http.request.env['module81.module81'].search([]),
#         })

#     @http.route('/module81/module81/objects/<model("module81.module81"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module81.object', {
#             'object': obj
#         })