# -*- coding: utf-8 -*-
from odoo import http

# class Module166(http.Controller):
#     @http.route('/module166/module166/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module166/module166/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module166.listing', {
#             'root': '/module166/module166',
#             'objects': http.request.env['module166.module166'].search([]),
#         })

#     @http.route('/module166/module166/objects/<model("module166.module166"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module166.object', {
#             'object': obj
#         })