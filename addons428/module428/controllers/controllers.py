# -*- coding: utf-8 -*-
from odoo import http

# class Module428(http.Controller):
#     @http.route('/module428/module428/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module428/module428/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module428.listing', {
#             'root': '/module428/module428',
#             'objects': http.request.env['module428.module428'].search([]),
#         })

#     @http.route('/module428/module428/objects/<model("module428.module428"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module428.object', {
#             'object': obj
#         })