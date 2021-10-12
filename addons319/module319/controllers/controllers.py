# -*- coding: utf-8 -*-
from odoo import http

# class Module319(http.Controller):
#     @http.route('/module319/module319/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module319/module319/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module319.listing', {
#             'root': '/module319/module319',
#             'objects': http.request.env['module319.module319'].search([]),
#         })

#     @http.route('/module319/module319/objects/<model("module319.module319"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module319.object', {
#             'object': obj
#         })