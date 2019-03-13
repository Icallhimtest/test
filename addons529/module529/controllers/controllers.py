# -*- coding: utf-8 -*-
from odoo import http

# class Module529(http.Controller):
#     @http.route('/module529/module529/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module529/module529/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module529.listing', {
#             'root': '/module529/module529',
#             'objects': http.request.env['module529.module529'].search([]),
#         })

#     @http.route('/module529/module529/objects/<model("module529.module529"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module529.object', {
#             'object': obj
#         })