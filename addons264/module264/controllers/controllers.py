# -*- coding: utf-8 -*-
from odoo import http

# class Module264(http.Controller):
#     @http.route('/module264/module264/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module264/module264/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module264.listing', {
#             'root': '/module264/module264',
#             'objects': http.request.env['module264.module264'].search([]),
#         })

#     @http.route('/module264/module264/objects/<model("module264.module264"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module264.object', {
#             'object': obj
#         })