# -*- coding: utf-8 -*-
from odoo import http

# class Module110(http.Controller):
#     @http.route('/module110/module110/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module110/module110/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module110.listing', {
#             'root': '/module110/module110',
#             'objects': http.request.env['module110.module110'].search([]),
#         })

#     @http.route('/module110/module110/objects/<model("module110.module110"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module110.object', {
#             'object': obj
#         })