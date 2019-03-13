# -*- coding: utf-8 -*-
from odoo import http

# class Module211(http.Controller):
#     @http.route('/module211/module211/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module211/module211/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module211.listing', {
#             'root': '/module211/module211',
#             'objects': http.request.env['module211.module211'].search([]),
#         })

#     @http.route('/module211/module211/objects/<model("module211.module211"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module211.object', {
#             'object': obj
#         })