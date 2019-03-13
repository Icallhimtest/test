# -*- coding: utf-8 -*-
from odoo import http

# class Module310(http.Controller):
#     @http.route('/module310/module310/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module310/module310/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module310.listing', {
#             'root': '/module310/module310',
#             'objects': http.request.env['module310.module310'].search([]),
#         })

#     @http.route('/module310/module310/objects/<model("module310.module310"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module310.object', {
#             'object': obj
#         })