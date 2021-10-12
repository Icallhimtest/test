# -*- coding: utf-8 -*-
from odoo import http

# class Module61(http.Controller):
#     @http.route('/module61/module61/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module61/module61/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module61.listing', {
#             'root': '/module61/module61',
#             'objects': http.request.env['module61.module61'].search([]),
#         })

#     @http.route('/module61/module61/objects/<model("module61.module61"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module61.object', {
#             'object': obj
#         })