# -*- coding: utf-8 -*-
from odoo import http

# class Module389(http.Controller):
#     @http.route('/module389/module389/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module389/module389/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module389.listing', {
#             'root': '/module389/module389',
#             'objects': http.request.env['module389.module389'].search([]),
#         })

#     @http.route('/module389/module389/objects/<model("module389.module389"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module389.object', {
#             'object': obj
#         })