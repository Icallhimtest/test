# -*- coding: utf-8 -*-
from odoo import http

# class Module235(http.Controller):
#     @http.route('/module235/module235/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module235/module235/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module235.listing', {
#             'root': '/module235/module235',
#             'objects': http.request.env['module235.module235'].search([]),
#         })

#     @http.route('/module235/module235/objects/<model("module235.module235"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module235.object', {
#             'object': obj
#         })