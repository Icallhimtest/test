# -*- coding: utf-8 -*-
from odoo import http

# class Module482(http.Controller):
#     @http.route('/module482/module482/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module482/module482/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module482.listing', {
#             'root': '/module482/module482',
#             'objects': http.request.env['module482.module482'].search([]),
#         })

#     @http.route('/module482/module482/objects/<model("module482.module482"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module482.object', {
#             'object': obj
#         })