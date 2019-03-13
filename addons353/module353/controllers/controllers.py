# -*- coding: utf-8 -*-
from odoo import http

# class Module353(http.Controller):
#     @http.route('/module353/module353/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module353/module353/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module353.listing', {
#             'root': '/module353/module353',
#             'objects': http.request.env['module353.module353'].search([]),
#         })

#     @http.route('/module353/module353/objects/<model("module353.module353"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module353.object', {
#             'object': obj
#         })