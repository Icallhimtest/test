# -*- coding: utf-8 -*-
from odoo import http

# class Module417(http.Controller):
#     @http.route('/module417/module417/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module417/module417/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module417.listing', {
#             'root': '/module417/module417',
#             'objects': http.request.env['module417.module417'].search([]),
#         })

#     @http.route('/module417/module417/objects/<model("module417.module417"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module417.object', {
#             'object': obj
#         })