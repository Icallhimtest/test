# -*- coding: utf-8 -*-
from odoo import http

# class Module304(http.Controller):
#     @http.route('/module304/module304/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module304/module304/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module304.listing', {
#             'root': '/module304/module304',
#             'objects': http.request.env['module304.module304'].search([]),
#         })

#     @http.route('/module304/module304/objects/<model("module304.module304"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module304.object', {
#             'object': obj
#         })