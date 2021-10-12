# -*- coding: utf-8 -*-
from odoo import http

# class Module54(http.Controller):
#     @http.route('/module54/module54/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module54/module54/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module54.listing', {
#             'root': '/module54/module54',
#             'objects': http.request.env['module54.module54'].search([]),
#         })

#     @http.route('/module54/module54/objects/<model("module54.module54"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module54.object', {
#             'object': obj
#         })