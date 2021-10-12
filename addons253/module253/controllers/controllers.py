# -*- coding: utf-8 -*-
from odoo import http

# class Module253(http.Controller):
#     @http.route('/module253/module253/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module253/module253/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module253.listing', {
#             'root': '/module253/module253',
#             'objects': http.request.env['module253.module253'].search([]),
#         })

#     @http.route('/module253/module253/objects/<model("module253.module253"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module253.object', {
#             'object': obj
#         })