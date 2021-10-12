# -*- coding: utf-8 -*-
from odoo import http

# class Module227(http.Controller):
#     @http.route('/module227/module227/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module227/module227/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module227.listing', {
#             'root': '/module227/module227',
#             'objects': http.request.env['module227.module227'].search([]),
#         })

#     @http.route('/module227/module227/objects/<model("module227.module227"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module227.object', {
#             'object': obj
#         })