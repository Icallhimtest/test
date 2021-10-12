# -*- coding: utf-8 -*-
from odoo import http

# class Module265(http.Controller):
#     @http.route('/module265/module265/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module265/module265/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module265.listing', {
#             'root': '/module265/module265',
#             'objects': http.request.env['module265.module265'].search([]),
#         })

#     @http.route('/module265/module265/objects/<model("module265.module265"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module265.object', {
#             'object': obj
#         })