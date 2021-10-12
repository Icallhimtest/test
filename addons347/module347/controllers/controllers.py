# -*- coding: utf-8 -*-
from odoo import http

# class Module347(http.Controller):
#     @http.route('/module347/module347/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module347/module347/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module347.listing', {
#             'root': '/module347/module347',
#             'objects': http.request.env['module347.module347'].search([]),
#         })

#     @http.route('/module347/module347/objects/<model("module347.module347"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module347.object', {
#             'object': obj
#         })