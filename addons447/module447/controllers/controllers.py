# -*- coding: utf-8 -*-
from odoo import http

# class Module447(http.Controller):
#     @http.route('/module447/module447/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module447/module447/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module447.listing', {
#             'root': '/module447/module447',
#             'objects': http.request.env['module447.module447'].search([]),
#         })

#     @http.route('/module447/module447/objects/<model("module447.module447"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module447.object', {
#             'object': obj
#         })