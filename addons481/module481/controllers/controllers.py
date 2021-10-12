# -*- coding: utf-8 -*-
from odoo import http

# class Module481(http.Controller):
#     @http.route('/module481/module481/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module481/module481/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module481.listing', {
#             'root': '/module481/module481',
#             'objects': http.request.env['module481.module481'].search([]),
#         })

#     @http.route('/module481/module481/objects/<model("module481.module481"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module481.object', {
#             'object': obj
#         })