# -*- coding: utf-8 -*-
from odoo import http

# class Module373(http.Controller):
#     @http.route('/module373/module373/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module373/module373/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module373.listing', {
#             'root': '/module373/module373',
#             'objects': http.request.env['module373.module373'].search([]),
#         })

#     @http.route('/module373/module373/objects/<model("module373.module373"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module373.object', {
#             'object': obj
#         })