# -*- coding: utf-8 -*-
from odoo import http

# class Module266(http.Controller):
#     @http.route('/module266/module266/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module266/module266/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module266.listing', {
#             'root': '/module266/module266',
#             'objects': http.request.env['module266.module266'].search([]),
#         })

#     @http.route('/module266/module266/objects/<model("module266.module266"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module266.object', {
#             'object': obj
#         })