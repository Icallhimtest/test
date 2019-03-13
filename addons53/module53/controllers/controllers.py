# -*- coding: utf-8 -*-
from odoo import http

# class Module53(http.Controller):
#     @http.route('/module53/module53/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module53/module53/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module53.listing', {
#             'root': '/module53/module53',
#             'objects': http.request.env['module53.module53'].search([]),
#         })

#     @http.route('/module53/module53/objects/<model("module53.module53"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module53.object', {
#             'object': obj
#         })