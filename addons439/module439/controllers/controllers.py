# -*- coding: utf-8 -*-
from odoo import http

# class Module439(http.Controller):
#     @http.route('/module439/module439/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module439/module439/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module439.listing', {
#             'root': '/module439/module439',
#             'objects': http.request.env['module439.module439'].search([]),
#         })

#     @http.route('/module439/module439/objects/<model("module439.module439"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module439.object', {
#             'object': obj
#         })