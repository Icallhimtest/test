# -*- coding: utf-8 -*-
from odoo import http

# class Module280(http.Controller):
#     @http.route('/module280/module280/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module280/module280/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module280.listing', {
#             'root': '/module280/module280',
#             'objects': http.request.env['module280.module280'].search([]),
#         })

#     @http.route('/module280/module280/objects/<model("module280.module280"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module280.object', {
#             'object': obj
#         })