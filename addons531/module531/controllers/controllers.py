# -*- coding: utf-8 -*-
from odoo import http

# class Module531(http.Controller):
#     @http.route('/module531/module531/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module531/module531/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module531.listing', {
#             'root': '/module531/module531',
#             'objects': http.request.env['module531.module531'].search([]),
#         })

#     @http.route('/module531/module531/objects/<model("module531.module531"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module531.object', {
#             'object': obj
#         })