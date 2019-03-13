# -*- coding: utf-8 -*-
from odoo import http

# class Module94(http.Controller):
#     @http.route('/module94/module94/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module94/module94/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module94.listing', {
#             'root': '/module94/module94',
#             'objects': http.request.env['module94.module94'].search([]),
#         })

#     @http.route('/module94/module94/objects/<model("module94.module94"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module94.object', {
#             'object': obj
#         })