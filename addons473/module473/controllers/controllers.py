# -*- coding: utf-8 -*-
from odoo import http

# class Module473(http.Controller):
#     @http.route('/module473/module473/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module473/module473/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module473.listing', {
#             'root': '/module473/module473',
#             'objects': http.request.env['module473.module473'].search([]),
#         })

#     @http.route('/module473/module473/objects/<model("module473.module473"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module473.object', {
#             'object': obj
#         })