# -*- coding: utf-8 -*-
from odoo import http

# class Module293(http.Controller):
#     @http.route('/module293/module293/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module293/module293/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module293.listing', {
#             'root': '/module293/module293',
#             'objects': http.request.env['module293.module293'].search([]),
#         })

#     @http.route('/module293/module293/objects/<model("module293.module293"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module293.object', {
#             'object': obj
#         })