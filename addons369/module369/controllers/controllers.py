# -*- coding: utf-8 -*-
from odoo import http

# class Module369(http.Controller):
#     @http.route('/module369/module369/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module369/module369/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module369.listing', {
#             'root': '/module369/module369',
#             'objects': http.request.env['module369.module369'].search([]),
#         })

#     @http.route('/module369/module369/objects/<model("module369.module369"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module369.object', {
#             'object': obj
#         })