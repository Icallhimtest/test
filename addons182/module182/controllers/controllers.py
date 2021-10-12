# -*- coding: utf-8 -*-
from odoo import http

# class Module182(http.Controller):
#     @http.route('/module182/module182/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module182/module182/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module182.listing', {
#             'root': '/module182/module182',
#             'objects': http.request.env['module182.module182'].search([]),
#         })

#     @http.route('/module182/module182/objects/<model("module182.module182"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module182.object', {
#             'object': obj
#         })