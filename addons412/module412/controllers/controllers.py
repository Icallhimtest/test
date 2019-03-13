# -*- coding: utf-8 -*-
from odoo import http

# class Module412(http.Controller):
#     @http.route('/module412/module412/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module412/module412/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module412.listing', {
#             'root': '/module412/module412',
#             'objects': http.request.env['module412.module412'].search([]),
#         })

#     @http.route('/module412/module412/objects/<model("module412.module412"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module412.object', {
#             'object': obj
#         })