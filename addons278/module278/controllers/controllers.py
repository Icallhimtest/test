# -*- coding: utf-8 -*-
from odoo import http

# class Module278(http.Controller):
#     @http.route('/module278/module278/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module278/module278/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module278.listing', {
#             'root': '/module278/module278',
#             'objects': http.request.env['module278.module278'].search([]),
#         })

#     @http.route('/module278/module278/objects/<model("module278.module278"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module278.object', {
#             'object': obj
#         })