# -*- coding: utf-8 -*-
from odoo import http

# class Module506(http.Controller):
#     @http.route('/module506/module506/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module506/module506/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module506.listing', {
#             'root': '/module506/module506',
#             'objects': http.request.env['module506.module506'].search([]),
#         })

#     @http.route('/module506/module506/objects/<model("module506.module506"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module506.object', {
#             'object': obj
#         })