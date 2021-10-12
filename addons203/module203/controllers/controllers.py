# -*- coding: utf-8 -*-
from odoo import http

# class Module203(http.Controller):
#     @http.route('/module203/module203/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module203/module203/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module203.listing', {
#             'root': '/module203/module203',
#             'objects': http.request.env['module203.module203'].search([]),
#         })

#     @http.route('/module203/module203/objects/<model("module203.module203"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module203.object', {
#             'object': obj
#         })