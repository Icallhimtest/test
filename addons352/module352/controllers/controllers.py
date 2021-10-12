# -*- coding: utf-8 -*-
from odoo import http

# class Module352(http.Controller):
#     @http.route('/module352/module352/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module352/module352/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module352.listing', {
#             'root': '/module352/module352',
#             'objects': http.request.env['module352.module352'].search([]),
#         })

#     @http.route('/module352/module352/objects/<model("module352.module352"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module352.object', {
#             'object': obj
#         })