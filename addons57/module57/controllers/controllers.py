# -*- coding: utf-8 -*-
from odoo import http

# class Module57(http.Controller):
#     @http.route('/module57/module57/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module57/module57/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module57.listing', {
#             'root': '/module57/module57',
#             'objects': http.request.env['module57.module57'].search([]),
#         })

#     @http.route('/module57/module57/objects/<model("module57.module57"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module57.object', {
#             'object': obj
#         })