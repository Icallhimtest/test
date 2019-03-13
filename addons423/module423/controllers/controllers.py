# -*- coding: utf-8 -*-
from odoo import http

# class Module423(http.Controller):
#     @http.route('/module423/module423/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module423/module423/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module423.listing', {
#             'root': '/module423/module423',
#             'objects': http.request.env['module423.module423'].search([]),
#         })

#     @http.route('/module423/module423/objects/<model("module423.module423"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module423.object', {
#             'object': obj
#         })