# -*- coding: utf-8 -*-
from odoo import http

# class Module465(http.Controller):
#     @http.route('/module465/module465/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module465/module465/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module465.listing', {
#             'root': '/module465/module465',
#             'objects': http.request.env['module465.module465'].search([]),
#         })

#     @http.route('/module465/module465/objects/<model("module465.module465"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module465.object', {
#             'object': obj
#         })