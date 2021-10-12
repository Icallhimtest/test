# -*- coding: utf-8 -*-
from odoo import http

# class Module39(http.Controller):
#     @http.route('/module39/module39/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module39/module39/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module39.listing', {
#             'root': '/module39/module39',
#             'objects': http.request.env['module39.module39'].search([]),
#         })

#     @http.route('/module39/module39/objects/<model("module39.module39"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module39.object', {
#             'object': obj
#         })