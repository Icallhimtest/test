# -*- coding: utf-8 -*-
from odoo import http

# class Module348(http.Controller):
#     @http.route('/module348/module348/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module348/module348/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module348.listing', {
#             'root': '/module348/module348',
#             'objects': http.request.env['module348.module348'].search([]),
#         })

#     @http.route('/module348/module348/objects/<model("module348.module348"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module348.object', {
#             'object': obj
#         })