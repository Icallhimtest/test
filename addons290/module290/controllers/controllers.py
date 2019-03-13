# -*- coding: utf-8 -*-
from odoo import http

# class Module290(http.Controller):
#     @http.route('/module290/module290/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module290/module290/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module290.listing', {
#             'root': '/module290/module290',
#             'objects': http.request.env['module290.module290'].search([]),
#         })

#     @http.route('/module290/module290/objects/<model("module290.module290"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module290.object', {
#             'object': obj
#         })