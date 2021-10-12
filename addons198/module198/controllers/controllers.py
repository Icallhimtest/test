# -*- coding: utf-8 -*-
from odoo import http

# class Module198(http.Controller):
#     @http.route('/module198/module198/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module198/module198/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module198.listing', {
#             'root': '/module198/module198',
#             'objects': http.request.env['module198.module198'].search([]),
#         })

#     @http.route('/module198/module198/objects/<model("module198.module198"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module198.object', {
#             'object': obj
#         })