# -*- coding: utf-8 -*-
from odoo import http

# class Module419(http.Controller):
#     @http.route('/module419/module419/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module419/module419/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module419.listing', {
#             'root': '/module419/module419',
#             'objects': http.request.env['module419.module419'].search([]),
#         })

#     @http.route('/module419/module419/objects/<model("module419.module419"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module419.object', {
#             'object': obj
#         })