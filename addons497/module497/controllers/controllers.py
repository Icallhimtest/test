# -*- coding: utf-8 -*-
from odoo import http

# class Module497(http.Controller):
#     @http.route('/module497/module497/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module497/module497/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module497.listing', {
#             'root': '/module497/module497',
#             'objects': http.request.env['module497.module497'].search([]),
#         })

#     @http.route('/module497/module497/objects/<model("module497.module497"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module497.object', {
#             'object': obj
#         })