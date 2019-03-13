# -*- coding: utf-8 -*-
from odoo import http

# class Module128(http.Controller):
#     @http.route('/module128/module128/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module128/module128/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module128.listing', {
#             'root': '/module128/module128',
#             'objects': http.request.env['module128.module128'].search([]),
#         })

#     @http.route('/module128/module128/objects/<model("module128.module128"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module128.object', {
#             'object': obj
#         })