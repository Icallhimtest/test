# -*- coding: utf-8 -*-
from odoo import http

# class Module126(http.Controller):
#     @http.route('/module126/module126/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module126/module126/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module126.listing', {
#             'root': '/module126/module126',
#             'objects': http.request.env['module126.module126'].search([]),
#         })

#     @http.route('/module126/module126/objects/<model("module126.module126"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module126.object', {
#             'object': obj
#         })