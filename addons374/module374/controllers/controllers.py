# -*- coding: utf-8 -*-
from odoo import http

# class Module374(http.Controller):
#     @http.route('/module374/module374/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module374/module374/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module374.listing', {
#             'root': '/module374/module374',
#             'objects': http.request.env['module374.module374'].search([]),
#         })

#     @http.route('/module374/module374/objects/<model("module374.module374"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module374.object', {
#             'object': obj
#         })