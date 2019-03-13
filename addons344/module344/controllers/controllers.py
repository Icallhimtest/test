# -*- coding: utf-8 -*-
from odoo import http

# class Module344(http.Controller):
#     @http.route('/module344/module344/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module344/module344/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module344.listing', {
#             'root': '/module344/module344',
#             'objects': http.request.env['module344.module344'].search([]),
#         })

#     @http.route('/module344/module344/objects/<model("module344.module344"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module344.object', {
#             'object': obj
#         })