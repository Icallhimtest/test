# -*- coding: utf-8 -*-
from odoo import http

# class Module70(http.Controller):
#     @http.route('/module70/module70/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module70/module70/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module70.listing', {
#             'root': '/module70/module70',
#             'objects': http.request.env['module70.module70'].search([]),
#         })

#     @http.route('/module70/module70/objects/<model("module70.module70"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module70.object', {
#             'object': obj
#         })