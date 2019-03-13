# -*- coding: utf-8 -*-
from odoo import http

# class Module277(http.Controller):
#     @http.route('/module277/module277/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module277/module277/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module277.listing', {
#             'root': '/module277/module277',
#             'objects': http.request.env['module277.module277'].search([]),
#         })

#     @http.route('/module277/module277/objects/<model("module277.module277"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module277.object', {
#             'object': obj
#         })