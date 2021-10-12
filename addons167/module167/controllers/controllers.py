# -*- coding: utf-8 -*-
from odoo import http

# class Module167(http.Controller):
#     @http.route('/module167/module167/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module167/module167/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module167.listing', {
#             'root': '/module167/module167',
#             'objects': http.request.env['module167.module167'].search([]),
#         })

#     @http.route('/module167/module167/objects/<model("module167.module167"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module167.object', {
#             'object': obj
#         })