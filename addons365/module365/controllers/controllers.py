# -*- coding: utf-8 -*-
from odoo import http

# class Module365(http.Controller):
#     @http.route('/module365/module365/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module365/module365/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module365.listing', {
#             'root': '/module365/module365',
#             'objects': http.request.env['module365.module365'].search([]),
#         })

#     @http.route('/module365/module365/objects/<model("module365.module365"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module365.object', {
#             'object': obj
#         })