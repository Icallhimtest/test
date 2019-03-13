# -*- coding: utf-8 -*-
from odoo import http

# class Module390(http.Controller):
#     @http.route('/module390/module390/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module390/module390/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module390.listing', {
#             'root': '/module390/module390',
#             'objects': http.request.env['module390.module390'].search([]),
#         })

#     @http.route('/module390/module390/objects/<model("module390.module390"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module390.object', {
#             'object': obj
#         })