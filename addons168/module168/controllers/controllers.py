# -*- coding: utf-8 -*-
from odoo import http

# class Module168(http.Controller):
#     @http.route('/module168/module168/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module168/module168/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module168.listing', {
#             'root': '/module168/module168',
#             'objects': http.request.env['module168.module168'].search([]),
#         })

#     @http.route('/module168/module168/objects/<model("module168.module168"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module168.object', {
#             'object': obj
#         })