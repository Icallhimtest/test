# -*- coding: utf-8 -*-
from odoo import http

# class Module342(http.Controller):
#     @http.route('/module342/module342/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module342/module342/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module342.listing', {
#             'root': '/module342/module342',
#             'objects': http.request.env['module342.module342'].search([]),
#         })

#     @http.route('/module342/module342/objects/<model("module342.module342"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module342.object', {
#             'object': obj
#         })