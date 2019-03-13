# -*- coding: utf-8 -*-
from odoo import http

# class Module237(http.Controller):
#     @http.route('/module237/module237/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module237/module237/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module237.listing', {
#             'root': '/module237/module237',
#             'objects': http.request.env['module237.module237'].search([]),
#         })

#     @http.route('/module237/module237/objects/<model("module237.module237"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module237.object', {
#             'object': obj
#         })