# -*- coding: utf-8 -*-
from odoo import http

# class Module17(http.Controller):
#     @http.route('/module17/module17/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module17/module17/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module17.listing', {
#             'root': '/module17/module17',
#             'objects': http.request.env['module17.module17'].search([]),
#         })

#     @http.route('/module17/module17/objects/<model("module17.module17"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module17.object', {
#             'object': obj
#         })