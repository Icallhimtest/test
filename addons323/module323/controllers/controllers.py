# -*- coding: utf-8 -*-
from odoo import http

# class Module323(http.Controller):
#     @http.route('/module323/module323/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module323/module323/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module323.listing', {
#             'root': '/module323/module323',
#             'objects': http.request.env['module323.module323'].search([]),
#         })

#     @http.route('/module323/module323/objects/<model("module323.module323"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module323.object', {
#             'object': obj
#         })