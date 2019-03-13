# -*- coding: utf-8 -*-
from odoo import http

# class Module430(http.Controller):
#     @http.route('/module430/module430/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module430/module430/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module430.listing', {
#             'root': '/module430/module430',
#             'objects': http.request.env['module430.module430'].search([]),
#         })

#     @http.route('/module430/module430/objects/<model("module430.module430"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module430.object', {
#             'object': obj
#         })