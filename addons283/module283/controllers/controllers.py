# -*- coding: utf-8 -*-
from odoo import http

# class Module283(http.Controller):
#     @http.route('/module283/module283/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module283/module283/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module283.listing', {
#             'root': '/module283/module283',
#             'objects': http.request.env['module283.module283'].search([]),
#         })

#     @http.route('/module283/module283/objects/<model("module283.module283"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module283.object', {
#             'object': obj
#         })