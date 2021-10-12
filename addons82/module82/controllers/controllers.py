# -*- coding: utf-8 -*-
from odoo import http

# class Module82(http.Controller):
#     @http.route('/module82/module82/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module82/module82/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module82.listing', {
#             'root': '/module82/module82',
#             'objects': http.request.env['module82.module82'].search([]),
#         })

#     @http.route('/module82/module82/objects/<model("module82.module82"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module82.object', {
#             'object': obj
#         })