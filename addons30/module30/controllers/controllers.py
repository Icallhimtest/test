# -*- coding: utf-8 -*-
from odoo import http

# class Module30(http.Controller):
#     @http.route('/module30/module30/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module30/module30/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module30.listing', {
#             'root': '/module30/module30',
#             'objects': http.request.env['module30.module30'].search([]),
#         })

#     @http.route('/module30/module30/objects/<model("module30.module30"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module30.object', {
#             'object': obj
#         })