# -*- coding: utf-8 -*-
from odoo import http

# class Module354(http.Controller):
#     @http.route('/module354/module354/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module354/module354/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module354.listing', {
#             'root': '/module354/module354',
#             'objects': http.request.env['module354.module354'].search([]),
#         })

#     @http.route('/module354/module354/objects/<model("module354.module354"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module354.object', {
#             'object': obj
#         })