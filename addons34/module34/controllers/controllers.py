# -*- coding: utf-8 -*-
from odoo import http

# class Module34(http.Controller):
#     @http.route('/module34/module34/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module34/module34/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module34.listing', {
#             'root': '/module34/module34',
#             'objects': http.request.env['module34.module34'].search([]),
#         })

#     @http.route('/module34/module34/objects/<model("module34.module34"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module34.object', {
#             'object': obj
#         })