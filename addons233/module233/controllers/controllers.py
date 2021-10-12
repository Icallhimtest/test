# -*- coding: utf-8 -*-
from odoo import http

# class Module233(http.Controller):
#     @http.route('/module233/module233/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module233/module233/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module233.listing', {
#             'root': '/module233/module233',
#             'objects': http.request.env['module233.module233'].search([]),
#         })

#     @http.route('/module233/module233/objects/<model("module233.module233"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module233.object', {
#             'object': obj
#         })