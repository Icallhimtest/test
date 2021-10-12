# -*- coding: utf-8 -*-
from odoo import http

# class Module90(http.Controller):
#     @http.route('/module90/module90/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module90/module90/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module90.listing', {
#             'root': '/module90/module90',
#             'objects': http.request.env['module90.module90'].search([]),
#         })

#     @http.route('/module90/module90/objects/<model("module90.module90"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module90.object', {
#             'object': obj
#         })