# -*- coding: utf-8 -*-
from odoo import http

# class Module96(http.Controller):
#     @http.route('/module96/module96/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module96/module96/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module96.listing', {
#             'root': '/module96/module96',
#             'objects': http.request.env['module96.module96'].search([]),
#         })

#     @http.route('/module96/module96/objects/<model("module96.module96"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module96.object', {
#             'object': obj
#         })