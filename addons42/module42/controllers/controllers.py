# -*- coding: utf-8 -*-
from odoo import http

# class Module42(http.Controller):
#     @http.route('/module42/module42/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module42/module42/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module42.listing', {
#             'root': '/module42/module42',
#             'objects': http.request.env['module42.module42'].search([]),
#         })

#     @http.route('/module42/module42/objects/<model("module42.module42"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module42.object', {
#             'object': obj
#         })