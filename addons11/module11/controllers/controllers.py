# -*- coding: utf-8 -*-
from odoo import http

# class Module11(http.Controller):
#     @http.route('/module11/module11/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module11/module11/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module11.listing', {
#             'root': '/module11/module11',
#             'objects': http.request.env['module11.module11'].search([]),
#         })

#     @http.route('/module11/module11/objects/<model("module11.module11"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module11.object', {
#             'object': obj
#         })