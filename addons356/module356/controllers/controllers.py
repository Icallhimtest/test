# -*- coding: utf-8 -*-
from odoo import http

# class Module356(http.Controller):
#     @http.route('/module356/module356/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module356/module356/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module356.listing', {
#             'root': '/module356/module356',
#             'objects': http.request.env['module356.module356'].search([]),
#         })

#     @http.route('/module356/module356/objects/<model("module356.module356"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module356.object', {
#             'object': obj
#         })