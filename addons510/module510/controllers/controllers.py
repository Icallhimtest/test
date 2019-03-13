# -*- coding: utf-8 -*-
from odoo import http

# class Module510(http.Controller):
#     @http.route('/module510/module510/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module510/module510/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module510.listing', {
#             'root': '/module510/module510',
#             'objects': http.request.env['module510.module510'].search([]),
#         })

#     @http.route('/module510/module510/objects/<model("module510.module510"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module510.object', {
#             'object': obj
#         })