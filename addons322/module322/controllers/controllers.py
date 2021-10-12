# -*- coding: utf-8 -*-
from odoo import http

# class Module322(http.Controller):
#     @http.route('/module322/module322/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module322/module322/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module322.listing', {
#             'root': '/module322/module322',
#             'objects': http.request.env['module322.module322'].search([]),
#         })

#     @http.route('/module322/module322/objects/<model("module322.module322"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module322.object', {
#             'object': obj
#         })