# -*- coding: utf-8 -*-
from odoo import http

# class Module98(http.Controller):
#     @http.route('/module98/module98/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module98/module98/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module98.listing', {
#             'root': '/module98/module98',
#             'objects': http.request.env['module98.module98'].search([]),
#         })

#     @http.route('/module98/module98/objects/<model("module98.module98"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module98.object', {
#             'object': obj
#         })