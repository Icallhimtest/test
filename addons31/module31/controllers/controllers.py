# -*- coding: utf-8 -*-
from odoo import http

# class Module31(http.Controller):
#     @http.route('/module31/module31/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module31/module31/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module31.listing', {
#             'root': '/module31/module31',
#             'objects': http.request.env['module31.module31'].search([]),
#         })

#     @http.route('/module31/module31/objects/<model("module31.module31"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module31.object', {
#             'object': obj
#         })