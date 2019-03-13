# -*- coding: utf-8 -*-
from odoo import http

# class Module209(http.Controller):
#     @http.route('/module209/module209/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module209/module209/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module209.listing', {
#             'root': '/module209/module209',
#             'objects': http.request.env['module209.module209'].search([]),
#         })

#     @http.route('/module209/module209/objects/<model("module209.module209"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module209.object', {
#             'object': obj
#         })