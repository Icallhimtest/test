# -*- coding: utf-8 -*-
from odoo import http

# class Module498(http.Controller):
#     @http.route('/module498/module498/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module498/module498/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module498.listing', {
#             'root': '/module498/module498',
#             'objects': http.request.env['module498.module498'].search([]),
#         })

#     @http.route('/module498/module498/objects/<model("module498.module498"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module498.object', {
#             'object': obj
#         })