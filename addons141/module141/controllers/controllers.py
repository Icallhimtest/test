# -*- coding: utf-8 -*-
from odoo import http

# class Module141(http.Controller):
#     @http.route('/module141/module141/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module141/module141/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module141.listing', {
#             'root': '/module141/module141',
#             'objects': http.request.env['module141.module141'].search([]),
#         })

#     @http.route('/module141/module141/objects/<model("module141.module141"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module141.object', {
#             'object': obj
#         })