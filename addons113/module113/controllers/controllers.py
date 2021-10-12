# -*- coding: utf-8 -*-
from odoo import http

# class Module113(http.Controller):
#     @http.route('/module113/module113/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module113/module113/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module113.listing', {
#             'root': '/module113/module113',
#             'objects': http.request.env['module113.module113'].search([]),
#         })

#     @http.route('/module113/module113/objects/<model("module113.module113"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module113.object', {
#             'object': obj
#         })