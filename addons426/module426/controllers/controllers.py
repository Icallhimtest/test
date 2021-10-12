# -*- coding: utf-8 -*-
from odoo import http

# class Module426(http.Controller):
#     @http.route('/module426/module426/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module426/module426/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module426.listing', {
#             'root': '/module426/module426',
#             'objects': http.request.env['module426.module426'].search([]),
#         })

#     @http.route('/module426/module426/objects/<model("module426.module426"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module426.object', {
#             'object': obj
#         })