# -*- coding: utf-8 -*-
from odoo import http

# class Module159(http.Controller):
#     @http.route('/module159/module159/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module159/module159/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module159.listing', {
#             'root': '/module159/module159',
#             'objects': http.request.env['module159.module159'].search([]),
#         })

#     @http.route('/module159/module159/objects/<model("module159.module159"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module159.object', {
#             'object': obj
#         })