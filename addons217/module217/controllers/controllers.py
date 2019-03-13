# -*- coding: utf-8 -*-
from odoo import http

# class Module217(http.Controller):
#     @http.route('/module217/module217/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module217/module217/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module217.listing', {
#             'root': '/module217/module217',
#             'objects': http.request.env['module217.module217'].search([]),
#         })

#     @http.route('/module217/module217/objects/<model("module217.module217"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module217.object', {
#             'object': obj
#         })