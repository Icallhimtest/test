# -*- coding: utf-8 -*-
from odoo import http

# class Module351(http.Controller):
#     @http.route('/module351/module351/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module351/module351/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module351.listing', {
#             'root': '/module351/module351',
#             'objects': http.request.env['module351.module351'].search([]),
#         })

#     @http.route('/module351/module351/objects/<model("module351.module351"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module351.object', {
#             'object': obj
#         })