# -*- coding: utf-8 -*-
from odoo import http

# class Module479(http.Controller):
#     @http.route('/module479/module479/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module479/module479/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module479.listing', {
#             'root': '/module479/module479',
#             'objects': http.request.env['module479.module479'].search([]),
#         })

#     @http.route('/module479/module479/objects/<model("module479.module479"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module479.object', {
#             'object': obj
#         })