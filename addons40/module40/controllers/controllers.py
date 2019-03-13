# -*- coding: utf-8 -*-
from odoo import http

# class Module40(http.Controller):
#     @http.route('/module40/module40/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module40/module40/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module40.listing', {
#             'root': '/module40/module40',
#             'objects': http.request.env['module40.module40'].search([]),
#         })

#     @http.route('/module40/module40/objects/<model("module40.module40"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module40.object', {
#             'object': obj
#         })