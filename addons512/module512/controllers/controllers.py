# -*- coding: utf-8 -*-
from odoo import http

# class Module512(http.Controller):
#     @http.route('/module512/module512/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module512/module512/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module512.listing', {
#             'root': '/module512/module512',
#             'objects': http.request.env['module512.module512'].search([]),
#         })

#     @http.route('/module512/module512/objects/<model("module512.module512"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module512.object', {
#             'object': obj
#         })