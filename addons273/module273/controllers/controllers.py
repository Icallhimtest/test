# -*- coding: utf-8 -*-
from odoo import http

# class Module273(http.Controller):
#     @http.route('/module273/module273/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module273/module273/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module273.listing', {
#             'root': '/module273/module273',
#             'objects': http.request.env['module273.module273'].search([]),
#         })

#     @http.route('/module273/module273/objects/<model("module273.module273"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module273.object', {
#             'object': obj
#         })