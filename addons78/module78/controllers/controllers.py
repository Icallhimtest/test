# -*- coding: utf-8 -*-
from odoo import http

# class Module78(http.Controller):
#     @http.route('/module78/module78/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module78/module78/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module78.listing', {
#             'root': '/module78/module78',
#             'objects': http.request.env['module78.module78'].search([]),
#         })

#     @http.route('/module78/module78/objects/<model("module78.module78"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module78.object', {
#             'object': obj
#         })