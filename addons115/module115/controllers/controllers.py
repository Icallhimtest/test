# -*- coding: utf-8 -*-
from odoo import http

# class Module115(http.Controller):
#     @http.route('/module115/module115/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module115/module115/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module115.listing', {
#             'root': '/module115/module115',
#             'objects': http.request.env['module115.module115'].search([]),
#         })

#     @http.route('/module115/module115/objects/<model("module115.module115"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module115.object', {
#             'object': obj
#         })