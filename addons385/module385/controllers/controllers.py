# -*- coding: utf-8 -*-
from odoo import http

# class Module385(http.Controller):
#     @http.route('/module385/module385/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module385/module385/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module385.listing', {
#             'root': '/module385/module385',
#             'objects': http.request.env['module385.module385'].search([]),
#         })

#     @http.route('/module385/module385/objects/<model("module385.module385"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module385.object', {
#             'object': obj
#         })