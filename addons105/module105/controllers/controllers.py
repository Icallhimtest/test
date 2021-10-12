# -*- coding: utf-8 -*-
from odoo import http

# class Module105(http.Controller):
#     @http.route('/module105/module105/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module105/module105/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module105.listing', {
#             'root': '/module105/module105',
#             'objects': http.request.env['module105.module105'].search([]),
#         })

#     @http.route('/module105/module105/objects/<model("module105.module105"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module105.object', {
#             'object': obj
#         })