# -*- coding: utf-8 -*-
from odoo import http

# class Module516(http.Controller):
#     @http.route('/module516/module516/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module516/module516/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module516.listing', {
#             'root': '/module516/module516',
#             'objects': http.request.env['module516.module516'].search([]),
#         })

#     @http.route('/module516/module516/objects/<model("module516.module516"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module516.object', {
#             'object': obj
#         })