# -*- coding: utf-8 -*-
from odoo import http

# class Module486(http.Controller):
#     @http.route('/module486/module486/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module486/module486/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module486.listing', {
#             'root': '/module486/module486',
#             'objects': http.request.env['module486.module486'].search([]),
#         })

#     @http.route('/module486/module486/objects/<model("module486.module486"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module486.object', {
#             'object': obj
#         })