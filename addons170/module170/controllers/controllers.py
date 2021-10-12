# -*- coding: utf-8 -*-
from odoo import http

# class Module170(http.Controller):
#     @http.route('/module170/module170/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module170/module170/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module170.listing', {
#             'root': '/module170/module170',
#             'objects': http.request.env['module170.module170'].search([]),
#         })

#     @http.route('/module170/module170/objects/<model("module170.module170"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module170.object', {
#             'object': obj
#         })