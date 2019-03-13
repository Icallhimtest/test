# -*- coding: utf-8 -*-
from odoo import http

# class Module294(http.Controller):
#     @http.route('/module294/module294/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module294/module294/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module294.listing', {
#             'root': '/module294/module294',
#             'objects': http.request.env['module294.module294'].search([]),
#         })

#     @http.route('/module294/module294/objects/<model("module294.module294"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module294.object', {
#             'object': obj
#         })