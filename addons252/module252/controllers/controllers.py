# -*- coding: utf-8 -*-
from odoo import http

# class Module252(http.Controller):
#     @http.route('/module252/module252/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module252/module252/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module252.listing', {
#             'root': '/module252/module252',
#             'objects': http.request.env['module252.module252'].search([]),
#         })

#     @http.route('/module252/module252/objects/<model("module252.module252"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module252.object', {
#             'object': obj
#         })