# -*- coding: utf-8 -*-
from odoo import http

# class Module292(http.Controller):
#     @http.route('/module292/module292/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module292/module292/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module292.listing', {
#             'root': '/module292/module292',
#             'objects': http.request.env['module292.module292'].search([]),
#         })

#     @http.route('/module292/module292/objects/<model("module292.module292"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module292.object', {
#             'object': obj
#         })