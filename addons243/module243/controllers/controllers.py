# -*- coding: utf-8 -*-
from odoo import http

# class Module243(http.Controller):
#     @http.route('/module243/module243/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module243/module243/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module243.listing', {
#             'root': '/module243/module243',
#             'objects': http.request.env['module243.module243'].search([]),
#         })

#     @http.route('/module243/module243/objects/<model("module243.module243"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module243.object', {
#             'object': obj
#         })