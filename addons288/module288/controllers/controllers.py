# -*- coding: utf-8 -*-
from odoo import http

# class Module288(http.Controller):
#     @http.route('/module288/module288/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module288/module288/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module288.listing', {
#             'root': '/module288/module288',
#             'objects': http.request.env['module288.module288'].search([]),
#         })

#     @http.route('/module288/module288/objects/<model("module288.module288"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module288.object', {
#             'object': obj
#         })