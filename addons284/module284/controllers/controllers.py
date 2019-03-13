# -*- coding: utf-8 -*-
from odoo import http

# class Module284(http.Controller):
#     @http.route('/module284/module284/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module284/module284/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module284.listing', {
#             'root': '/module284/module284',
#             'objects': http.request.env['module284.module284'].search([]),
#         })

#     @http.route('/module284/module284/objects/<model("module284.module284"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module284.object', {
#             'object': obj
#         })