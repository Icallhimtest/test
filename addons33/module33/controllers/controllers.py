# -*- coding: utf-8 -*-
from odoo import http

# class Module33(http.Controller):
#     @http.route('/module33/module33/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module33/module33/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module33.listing', {
#             'root': '/module33/module33',
#             'objects': http.request.env['module33.module33'].search([]),
#         })

#     @http.route('/module33/module33/objects/<model("module33.module33"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module33.object', {
#             'object': obj
#         })