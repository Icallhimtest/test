# -*- coding: utf-8 -*-
from odoo import http

# class Module308(http.Controller):
#     @http.route('/module308/module308/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module308/module308/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module308.listing', {
#             'root': '/module308/module308',
#             'objects': http.request.env['module308.module308'].search([]),
#         })

#     @http.route('/module308/module308/objects/<model("module308.module308"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module308.object', {
#             'object': obj
#         })