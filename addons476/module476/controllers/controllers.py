# -*- coding: utf-8 -*-
from odoo import http

# class Module476(http.Controller):
#     @http.route('/module476/module476/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module476/module476/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module476.listing', {
#             'root': '/module476/module476',
#             'objects': http.request.env['module476.module476'].search([]),
#         })

#     @http.route('/module476/module476/objects/<model("module476.module476"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module476.object', {
#             'object': obj
#         })