# -*- coding: utf-8 -*-
from odoo import http

# class Module261(http.Controller):
#     @http.route('/module261/module261/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module261/module261/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module261.listing', {
#             'root': '/module261/module261',
#             'objects': http.request.env['module261.module261'].search([]),
#         })

#     @http.route('/module261/module261/objects/<model("module261.module261"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module261.object', {
#             'object': obj
#         })