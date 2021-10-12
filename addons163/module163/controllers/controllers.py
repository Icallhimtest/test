# -*- coding: utf-8 -*-
from odoo import http

# class Module163(http.Controller):
#     @http.route('/module163/module163/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module163/module163/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module163.listing', {
#             'root': '/module163/module163',
#             'objects': http.request.env['module163.module163'].search([]),
#         })

#     @http.route('/module163/module163/objects/<model("module163.module163"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module163.object', {
#             'object': obj
#         })