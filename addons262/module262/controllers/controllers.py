# -*- coding: utf-8 -*-
from odoo import http

# class Module262(http.Controller):
#     @http.route('/module262/module262/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module262/module262/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module262.listing', {
#             'root': '/module262/module262',
#             'objects': http.request.env['module262.module262'].search([]),
#         })

#     @http.route('/module262/module262/objects/<model("module262.module262"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module262.object', {
#             'object': obj
#         })