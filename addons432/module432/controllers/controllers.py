# -*- coding: utf-8 -*-
from odoo import http

# class Module432(http.Controller):
#     @http.route('/module432/module432/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module432/module432/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module432.listing', {
#             'root': '/module432/module432',
#             'objects': http.request.env['module432.module432'].search([]),
#         })

#     @http.route('/module432/module432/objects/<model("module432.module432"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module432.object', {
#             'object': obj
#         })