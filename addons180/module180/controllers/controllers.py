# -*- coding: utf-8 -*-
from odoo import http

# class Module180(http.Controller):
#     @http.route('/module180/module180/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module180/module180/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module180.listing', {
#             'root': '/module180/module180',
#             'objects': http.request.env['module180.module180'].search([]),
#         })

#     @http.route('/module180/module180/objects/<model("module180.module180"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module180.object', {
#             'object': obj
#         })