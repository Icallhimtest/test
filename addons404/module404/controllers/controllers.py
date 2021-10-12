# -*- coding: utf-8 -*-
from odoo import http

# class Module404(http.Controller):
#     @http.route('/module404/module404/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module404/module404/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module404.listing', {
#             'root': '/module404/module404',
#             'objects': http.request.env['module404.module404'].search([]),
#         })

#     @http.route('/module404/module404/objects/<model("module404.module404"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module404.object', {
#             'object': obj
#         })