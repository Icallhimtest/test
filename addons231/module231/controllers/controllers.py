# -*- coding: utf-8 -*-
from odoo import http

# class Module231(http.Controller):
#     @http.route('/module231/module231/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module231/module231/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module231.listing', {
#             'root': '/module231/module231',
#             'objects': http.request.env['module231.module231'].search([]),
#         })

#     @http.route('/module231/module231/objects/<model("module231.module231"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module231.object', {
#             'object': obj
#         })