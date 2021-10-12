# -*- coding: utf-8 -*-
from odoo import http

# class Module268(http.Controller):
#     @http.route('/module268/module268/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module268/module268/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module268.listing', {
#             'root': '/module268/module268',
#             'objects': http.request.env['module268.module268'].search([]),
#         })

#     @http.route('/module268/module268/objects/<model("module268.module268"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module268.object', {
#             'object': obj
#         })