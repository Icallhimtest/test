# -*- coding: utf-8 -*-
from odoo import http

# class Module281(http.Controller):
#     @http.route('/module281/module281/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module281/module281/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module281.listing', {
#             'root': '/module281/module281',
#             'objects': http.request.env['module281.module281'].search([]),
#         })

#     @http.route('/module281/module281/objects/<model("module281.module281"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module281.object', {
#             'object': obj
#         })