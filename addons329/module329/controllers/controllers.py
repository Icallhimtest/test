# -*- coding: utf-8 -*-
from odoo import http

# class Module329(http.Controller):
#     @http.route('/module329/module329/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module329/module329/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module329.listing', {
#             'root': '/module329/module329',
#             'objects': http.request.env['module329.module329'].search([]),
#         })

#     @http.route('/module329/module329/objects/<model("module329.module329"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module329.object', {
#             'object': obj
#         })