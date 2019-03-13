# -*- coding: utf-8 -*-
from odoo import http

# class Module488(http.Controller):
#     @http.route('/module488/module488/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module488/module488/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module488.listing', {
#             'root': '/module488/module488',
#             'objects': http.request.env['module488.module488'].search([]),
#         })

#     @http.route('/module488/module488/objects/<model("module488.module488"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module488.object', {
#             'object': obj
#         })