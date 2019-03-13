# -*- coding: utf-8 -*-
from odoo import http

# class Module435(http.Controller):
#     @http.route('/module435/module435/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module435/module435/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module435.listing', {
#             'root': '/module435/module435',
#             'objects': http.request.env['module435.module435'].search([]),
#         })

#     @http.route('/module435/module435/objects/<model("module435.module435"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module435.object', {
#             'object': obj
#         })