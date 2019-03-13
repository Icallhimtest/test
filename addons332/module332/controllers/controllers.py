# -*- coding: utf-8 -*-
from odoo import http

# class Module332(http.Controller):
#     @http.route('/module332/module332/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module332/module332/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module332.listing', {
#             'root': '/module332/module332',
#             'objects': http.request.env['module332.module332'].search([]),
#         })

#     @http.route('/module332/module332/objects/<model("module332.module332"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module332.object', {
#             'object': obj
#         })