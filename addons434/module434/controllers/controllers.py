# -*- coding: utf-8 -*-
from odoo import http

# class Module434(http.Controller):
#     @http.route('/module434/module434/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module434/module434/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module434.listing', {
#             'root': '/module434/module434',
#             'objects': http.request.env['module434.module434'].search([]),
#         })

#     @http.route('/module434/module434/objects/<model("module434.module434"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module434.object', {
#             'object': obj
#         })