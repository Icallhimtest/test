# -*- coding: utf-8 -*-
from odoo import http

# class Module397(http.Controller):
#     @http.route('/module397/module397/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module397/module397/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module397.listing', {
#             'root': '/module397/module397',
#             'objects': http.request.env['module397.module397'].search([]),
#         })

#     @http.route('/module397/module397/objects/<model("module397.module397"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module397.object', {
#             'object': obj
#         })