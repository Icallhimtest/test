# -*- coding: utf-8 -*-
from odoo import http

# class Module51(http.Controller):
#     @http.route('/module51/module51/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module51/module51/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module51.listing', {
#             'root': '/module51/module51',
#             'objects': http.request.env['module51.module51'].search([]),
#         })

#     @http.route('/module51/module51/objects/<model("module51.module51"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module51.object', {
#             'object': obj
#         })