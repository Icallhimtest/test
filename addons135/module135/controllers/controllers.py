# -*- coding: utf-8 -*-
from odoo import http

# class Module135(http.Controller):
#     @http.route('/module135/module135/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module135/module135/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module135.listing', {
#             'root': '/module135/module135',
#             'objects': http.request.env['module135.module135'].search([]),
#         })

#     @http.route('/module135/module135/objects/<model("module135.module135"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module135.object', {
#             'object': obj
#         })