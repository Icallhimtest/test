# -*- coding: utf-8 -*-
from odoo import http

# class Module18(http.Controller):
#     @http.route('/module18/module18/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module18/module18/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module18.listing', {
#             'root': '/module18/module18',
#             'objects': http.request.env['module18.module18'].search([]),
#         })

#     @http.route('/module18/module18/objects/<model("module18.module18"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module18.object', {
#             'object': obj
#         })