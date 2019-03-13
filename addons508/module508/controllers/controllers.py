# -*- coding: utf-8 -*-
from odoo import http

# class Module508(http.Controller):
#     @http.route('/module508/module508/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module508/module508/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module508.listing', {
#             'root': '/module508/module508',
#             'objects': http.request.env['module508.module508'].search([]),
#         })

#     @http.route('/module508/module508/objects/<model("module508.module508"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module508.object', {
#             'object': obj
#         })