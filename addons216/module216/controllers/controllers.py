# -*- coding: utf-8 -*-
from odoo import http

# class Module216(http.Controller):
#     @http.route('/module216/module216/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module216/module216/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module216.listing', {
#             'root': '/module216/module216',
#             'objects': http.request.env['module216.module216'].search([]),
#         })

#     @http.route('/module216/module216/objects/<model("module216.module216"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module216.object', {
#             'object': obj
#         })