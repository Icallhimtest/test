# -*- coding: utf-8 -*-
from odoo import http

# class Module525(http.Controller):
#     @http.route('/module525/module525/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module525/module525/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module525.listing', {
#             'root': '/module525/module525',
#             'objects': http.request.env['module525.module525'].search([]),
#         })

#     @http.route('/module525/module525/objects/<model("module525.module525"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module525.object', {
#             'object': obj
#         })