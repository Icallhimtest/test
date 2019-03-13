# -*- coding: utf-8 -*-
from odoo import http

# class Module381(http.Controller):
#     @http.route('/module381/module381/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module381/module381/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module381.listing', {
#             'root': '/module381/module381',
#             'objects': http.request.env['module381.module381'].search([]),
#         })

#     @http.route('/module381/module381/objects/<model("module381.module381"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module381.object', {
#             'object': obj
#         })