# -*- coding: utf-8 -*-
from odoo import http

# class Module363(http.Controller):
#     @http.route('/module363/module363/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module363/module363/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module363.listing', {
#             'root': '/module363/module363',
#             'objects': http.request.env['module363.module363'].search([]),
#         })

#     @http.route('/module363/module363/objects/<model("module363.module363"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module363.object', {
#             'object': obj
#         })