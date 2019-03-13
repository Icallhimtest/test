# -*- coding: utf-8 -*-
from odoo import http

# class Module245(http.Controller):
#     @http.route('/module245/module245/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module245/module245/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module245.listing', {
#             'root': '/module245/module245',
#             'objects': http.request.env['module245.module245'].search([]),
#         })

#     @http.route('/module245/module245/objects/<model("module245.module245"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module245.object', {
#             'object': obj
#         })