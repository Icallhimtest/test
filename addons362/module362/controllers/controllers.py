# -*- coding: utf-8 -*-
from odoo import http

# class Module362(http.Controller):
#     @http.route('/module362/module362/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module362/module362/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module362.listing', {
#             'root': '/module362/module362',
#             'objects': http.request.env['module362.module362'].search([]),
#         })

#     @http.route('/module362/module362/objects/<model("module362.module362"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module362.object', {
#             'object': obj
#         })