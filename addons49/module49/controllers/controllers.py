# -*- coding: utf-8 -*-
from odoo import http

# class Module49(http.Controller):
#     @http.route('/module49/module49/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module49/module49/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module49.listing', {
#             'root': '/module49/module49',
#             'objects': http.request.env['module49.module49'].search([]),
#         })

#     @http.route('/module49/module49/objects/<model("module49.module49"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module49.object', {
#             'object': obj
#         })