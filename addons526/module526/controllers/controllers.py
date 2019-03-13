# -*- coding: utf-8 -*-
from odoo import http

# class Module526(http.Controller):
#     @http.route('/module526/module526/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module526/module526/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module526.listing', {
#             'root': '/module526/module526',
#             'objects': http.request.env['module526.module526'].search([]),
#         })

#     @http.route('/module526/module526/objects/<model("module526.module526"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module526.object', {
#             'object': obj
#         })