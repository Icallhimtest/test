# -*- coding: utf-8 -*-
from odoo import http

# class Module153(http.Controller):
#     @http.route('/module153/module153/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module153/module153/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module153.listing', {
#             'root': '/module153/module153',
#             'objects': http.request.env['module153.module153'].search([]),
#         })

#     @http.route('/module153/module153/objects/<model("module153.module153"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module153.object', {
#             'object': obj
#         })