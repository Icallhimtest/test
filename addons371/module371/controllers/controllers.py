# -*- coding: utf-8 -*-
from odoo import http

# class Module371(http.Controller):
#     @http.route('/module371/module371/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module371/module371/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module371.listing', {
#             'root': '/module371/module371',
#             'objects': http.request.env['module371.module371'].search([]),
#         })

#     @http.route('/module371/module371/objects/<model("module371.module371"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module371.object', {
#             'object': obj
#         })