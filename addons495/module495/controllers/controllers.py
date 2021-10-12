# -*- coding: utf-8 -*-
from odoo import http

# class Module495(http.Controller):
#     @http.route('/module495/module495/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module495/module495/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module495.listing', {
#             'root': '/module495/module495',
#             'objects': http.request.env['module495.module495'].search([]),
#         })

#     @http.route('/module495/module495/objects/<model("module495.module495"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module495.object', {
#             'object': obj
#         })