# -*- coding: utf-8 -*-
from odoo import http

# class Module47(http.Controller):
#     @http.route('/module47/module47/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module47/module47/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module47.listing', {
#             'root': '/module47/module47',
#             'objects': http.request.env['module47.module47'].search([]),
#         })

#     @http.route('/module47/module47/objects/<model("module47.module47"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module47.object', {
#             'object': obj
#         })