# -*- coding: utf-8 -*-
from odoo import http

# class Module28(http.Controller):
#     @http.route('/module28/module28/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module28/module28/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module28.listing', {
#             'root': '/module28/module28',
#             'objects': http.request.env['module28.module28'].search([]),
#         })

#     @http.route('/module28/module28/objects/<model("module28.module28"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module28.object', {
#             'object': obj
#         })