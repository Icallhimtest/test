# -*- coding: utf-8 -*-
from odoo import http

# class Module350(http.Controller):
#     @http.route('/module350/module350/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module350/module350/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module350.listing', {
#             'root': '/module350/module350',
#             'objects': http.request.env['module350.module350'].search([]),
#         })

#     @http.route('/module350/module350/objects/<model("module350.module350"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module350.object', {
#             'object': obj
#         })