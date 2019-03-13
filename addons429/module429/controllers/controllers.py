# -*- coding: utf-8 -*-
from odoo import http

# class Module429(http.Controller):
#     @http.route('/module429/module429/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module429/module429/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module429.listing', {
#             'root': '/module429/module429',
#             'objects': http.request.env['module429.module429'].search([]),
#         })

#     @http.route('/module429/module429/objects/<model("module429.module429"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module429.object', {
#             'object': obj
#         })