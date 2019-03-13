# -*- coding: utf-8 -*-
from odoo import http

# class Module248(http.Controller):
#     @http.route('/module248/module248/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module248/module248/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module248.listing', {
#             'root': '/module248/module248',
#             'objects': http.request.env['module248.module248'].search([]),
#         })

#     @http.route('/module248/module248/objects/<model("module248.module248"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module248.object', {
#             'object': obj
#         })