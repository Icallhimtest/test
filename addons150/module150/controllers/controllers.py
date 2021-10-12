# -*- coding: utf-8 -*-
from odoo import http

# class Module150(http.Controller):
#     @http.route('/module150/module150/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module150/module150/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module150.listing', {
#             'root': '/module150/module150',
#             'objects': http.request.env['module150.module150'].search([]),
#         })

#     @http.route('/module150/module150/objects/<model("module150.module150"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module150.object', {
#             'object': obj
#         })