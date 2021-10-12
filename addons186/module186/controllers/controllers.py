# -*- coding: utf-8 -*-
from odoo import http

# class Module186(http.Controller):
#     @http.route('/module186/module186/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module186/module186/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module186.listing', {
#             'root': '/module186/module186',
#             'objects': http.request.env['module186.module186'].search([]),
#         })

#     @http.route('/module186/module186/objects/<model("module186.module186"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module186.object', {
#             'object': obj
#         })