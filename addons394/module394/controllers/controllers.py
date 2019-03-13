# -*- coding: utf-8 -*-
from odoo import http

# class Module394(http.Controller):
#     @http.route('/module394/module394/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module394/module394/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module394.listing', {
#             'root': '/module394/module394',
#             'objects': http.request.env['module394.module394'].search([]),
#         })

#     @http.route('/module394/module394/objects/<model("module394.module394"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module394.object', {
#             'object': obj
#         })