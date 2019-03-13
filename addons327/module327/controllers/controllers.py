# -*- coding: utf-8 -*-
from odoo import http

# class Module327(http.Controller):
#     @http.route('/module327/module327/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module327/module327/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module327.listing', {
#             'root': '/module327/module327',
#             'objects': http.request.env['module327.module327'].search([]),
#         })

#     @http.route('/module327/module327/objects/<model("module327.module327"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module327.object', {
#             'object': obj
#         })