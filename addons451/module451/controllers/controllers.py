# -*- coding: utf-8 -*-
from odoo import http

# class Module451(http.Controller):
#     @http.route('/module451/module451/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module451/module451/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module451.listing', {
#             'root': '/module451/module451',
#             'objects': http.request.env['module451.module451'].search([]),
#         })

#     @http.route('/module451/module451/objects/<model("module451.module451"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module451.object', {
#             'object': obj
#         })