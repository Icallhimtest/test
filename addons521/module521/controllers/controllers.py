# -*- coding: utf-8 -*-
from odoo import http

# class Module521(http.Controller):
#     @http.route('/module521/module521/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module521/module521/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module521.listing', {
#             'root': '/module521/module521',
#             'objects': http.request.env['module521.module521'].search([]),
#         })

#     @http.route('/module521/module521/objects/<model("module521.module521"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module521.object', {
#             'object': obj
#         })