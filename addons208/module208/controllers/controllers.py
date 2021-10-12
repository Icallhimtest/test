# -*- coding: utf-8 -*-
from odoo import http

# class Module208(http.Controller):
#     @http.route('/module208/module208/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module208/module208/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module208.listing', {
#             'root': '/module208/module208',
#             'objects': http.request.env['module208.module208'].search([]),
#         })

#     @http.route('/module208/module208/objects/<model("module208.module208"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module208.object', {
#             'object': obj
#         })