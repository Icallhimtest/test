# -*- coding: utf-8 -*-
from odoo import http

# class Module528(http.Controller):
#     @http.route('/module528/module528/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module528/module528/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module528.listing', {
#             'root': '/module528/module528',
#             'objects': http.request.env['module528.module528'].search([]),
#         })

#     @http.route('/module528/module528/objects/<model("module528.module528"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module528.object', {
#             'object': obj
#         })