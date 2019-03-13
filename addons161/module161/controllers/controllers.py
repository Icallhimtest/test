# -*- coding: utf-8 -*-
from odoo import http

# class Module161(http.Controller):
#     @http.route('/module161/module161/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module161/module161/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module161.listing', {
#             'root': '/module161/module161',
#             'objects': http.request.env['module161.module161'].search([]),
#         })

#     @http.route('/module161/module161/objects/<model("module161.module161"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module161.object', {
#             'object': obj
#         })