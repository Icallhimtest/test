# -*- coding: utf-8 -*-
from odoo import http

# class Module199(http.Controller):
#     @http.route('/module199/module199/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module199/module199/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module199.listing', {
#             'root': '/module199/module199',
#             'objects': http.request.env['module199.module199'].search([]),
#         })

#     @http.route('/module199/module199/objects/<model("module199.module199"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module199.object', {
#             'object': obj
#         })