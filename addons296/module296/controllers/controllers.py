# -*- coding: utf-8 -*-
from odoo import http

# class Module296(http.Controller):
#     @http.route('/module296/module296/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module296/module296/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module296.listing', {
#             'root': '/module296/module296',
#             'objects': http.request.env['module296.module296'].search([]),
#         })

#     @http.route('/module296/module296/objects/<model("module296.module296"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module296.object', {
#             'object': obj
#         })