# -*- coding: utf-8 -*-
from odoo import http

# class Module202(http.Controller):
#     @http.route('/module202/module202/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module202/module202/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module202.listing', {
#             'root': '/module202/module202',
#             'objects': http.request.env['module202.module202'].search([]),
#         })

#     @http.route('/module202/module202/objects/<model("module202.module202"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module202.object', {
#             'object': obj
#         })