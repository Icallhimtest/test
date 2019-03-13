# -*- coding: utf-8 -*-
from odoo import http

# class Module152(http.Controller):
#     @http.route('/module152/module152/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module152/module152/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module152.listing', {
#             'root': '/module152/module152',
#             'objects': http.request.env['module152.module152'].search([]),
#         })

#     @http.route('/module152/module152/objects/<model("module152.module152"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module152.object', {
#             'object': obj
#         })