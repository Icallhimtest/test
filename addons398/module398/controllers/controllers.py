# -*- coding: utf-8 -*-
from odoo import http

# class Module398(http.Controller):
#     @http.route('/module398/module398/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module398/module398/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module398.listing', {
#             'root': '/module398/module398',
#             'objects': http.request.env['module398.module398'].search([]),
#         })

#     @http.route('/module398/module398/objects/<model("module398.module398"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module398.object', {
#             'object': obj
#         })