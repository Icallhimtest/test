# -*- coding: utf-8 -*-
from odoo import http

# class Module286(http.Controller):
#     @http.route('/module286/module286/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module286/module286/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module286.listing', {
#             'root': '/module286/module286',
#             'objects': http.request.env['module286.module286'].search([]),
#         })

#     @http.route('/module286/module286/objects/<model("module286.module286"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module286.object', {
#             'object': obj
#         })