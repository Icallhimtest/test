# -*- coding: utf-8 -*-
from odoo import http

# class Module368(http.Controller):
#     @http.route('/module368/module368/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module368/module368/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module368.listing', {
#             'root': '/module368/module368',
#             'objects': http.request.env['module368.module368'].search([]),
#         })

#     @http.route('/module368/module368/objects/<model("module368.module368"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module368.object', {
#             'object': obj
#         })