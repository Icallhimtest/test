# -*- coding: utf-8 -*-
from odoo import http

# class Module318(http.Controller):
#     @http.route('/module318/module318/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module318/module318/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module318.listing', {
#             'root': '/module318/module318',
#             'objects': http.request.env['module318.module318'].search([]),
#         })

#     @http.route('/module318/module318/objects/<model("module318.module318"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module318.object', {
#             'object': obj
#         })