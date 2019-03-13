# -*- coding: utf-8 -*-
from odoo import http

# class Module189(http.Controller):
#     @http.route('/module189/module189/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module189/module189/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module189.listing', {
#             'root': '/module189/module189',
#             'objects': http.request.env['module189.module189'].search([]),
#         })

#     @http.route('/module189/module189/objects/<model("module189.module189"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module189.object', {
#             'object': obj
#         })