# -*- coding: utf-8 -*-
from odoo import http

# class Module107(http.Controller):
#     @http.route('/module107/module107/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module107/module107/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module107.listing', {
#             'root': '/module107/module107',
#             'objects': http.request.env['module107.module107'].search([]),
#         })

#     @http.route('/module107/module107/objects/<model("module107.module107"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module107.object', {
#             'object': obj
#         })