# -*- coding: utf-8 -*-
from odoo import http

# class Module64(http.Controller):
#     @http.route('/module64/module64/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module64/module64/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module64.listing', {
#             'root': '/module64/module64',
#             'objects': http.request.env['module64.module64'].search([]),
#         })

#     @http.route('/module64/module64/objects/<model("module64.module64"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module64.object', {
#             'object': obj
#         })