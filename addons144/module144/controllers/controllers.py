# -*- coding: utf-8 -*-
from odoo import http

# class Module144(http.Controller):
#     @http.route('/module144/module144/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module144/module144/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module144.listing', {
#             'root': '/module144/module144',
#             'objects': http.request.env['module144.module144'].search([]),
#         })

#     @http.route('/module144/module144/objects/<model("module144.module144"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module144.object', {
#             'object': obj
#         })