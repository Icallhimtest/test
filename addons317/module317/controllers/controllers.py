# -*- coding: utf-8 -*-
from odoo import http

# class Module317(http.Controller):
#     @http.route('/module317/module317/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module317/module317/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module317.listing', {
#             'root': '/module317/module317',
#             'objects': http.request.env['module317.module317'].search([]),
#         })

#     @http.route('/module317/module317/objects/<model("module317.module317"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module317.object', {
#             'object': obj
#         })