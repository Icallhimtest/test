# -*- coding: utf-8 -*-
from odoo import http

# class Module172(http.Controller):
#     @http.route('/module172/module172/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module172/module172/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module172.listing', {
#             'root': '/module172/module172',
#             'objects': http.request.env['module172.module172'].search([]),
#         })

#     @http.route('/module172/module172/objects/<model("module172.module172"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module172.object', {
#             'object': obj
#         })