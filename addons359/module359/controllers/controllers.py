# -*- coding: utf-8 -*-
from odoo import http

# class Module359(http.Controller):
#     @http.route('/module359/module359/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module359/module359/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module359.listing', {
#             'root': '/module359/module359',
#             'objects': http.request.env['module359.module359'].search([]),
#         })

#     @http.route('/module359/module359/objects/<model("module359.module359"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module359.object', {
#             'object': obj
#         })