# -*- coding: utf-8 -*-
from odoo import http

# class Module134(http.Controller):
#     @http.route('/module134/module134/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module134/module134/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module134.listing', {
#             'root': '/module134/module134',
#             'objects': http.request.env['module134.module134'].search([]),
#         })

#     @http.route('/module134/module134/objects/<model("module134.module134"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module134.object', {
#             'object': obj
#         })