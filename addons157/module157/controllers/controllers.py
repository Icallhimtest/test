# -*- coding: utf-8 -*-
from odoo import http

# class Module157(http.Controller):
#     @http.route('/module157/module157/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module157/module157/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module157.listing', {
#             'root': '/module157/module157',
#             'objects': http.request.env['module157.module157'].search([]),
#         })

#     @http.route('/module157/module157/objects/<model("module157.module157"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module157.object', {
#             'object': obj
#         })