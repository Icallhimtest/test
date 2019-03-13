# -*- coding: utf-8 -*-
from odoo import http

# class Module91(http.Controller):
#     @http.route('/module91/module91/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module91/module91/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module91.listing', {
#             'root': '/module91/module91',
#             'objects': http.request.env['module91.module91'].search([]),
#         })

#     @http.route('/module91/module91/objects/<model("module91.module91"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module91.object', {
#             'object': obj
#         })