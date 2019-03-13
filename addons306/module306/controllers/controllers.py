# -*- coding: utf-8 -*-
from odoo import http

# class Module306(http.Controller):
#     @http.route('/module306/module306/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module306/module306/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module306.listing', {
#             'root': '/module306/module306',
#             'objects': http.request.env['module306.module306'].search([]),
#         })

#     @http.route('/module306/module306/objects/<model("module306.module306"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module306.object', {
#             'object': obj
#         })