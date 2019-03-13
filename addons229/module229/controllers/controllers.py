# -*- coding: utf-8 -*-
from odoo import http

# class Module229(http.Controller):
#     @http.route('/module229/module229/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module229/module229/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module229.listing', {
#             'root': '/module229/module229',
#             'objects': http.request.env['module229.module229'].search([]),
#         })

#     @http.route('/module229/module229/objects/<model("module229.module229"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module229.object', {
#             'object': obj
#         })