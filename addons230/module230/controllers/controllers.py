# -*- coding: utf-8 -*-
from odoo import http

# class Module230(http.Controller):
#     @http.route('/module230/module230/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module230/module230/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module230.listing', {
#             'root': '/module230/module230',
#             'objects': http.request.env['module230.module230'].search([]),
#         })

#     @http.route('/module230/module230/objects/<model("module230.module230"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module230.object', {
#             'object': obj
#         })