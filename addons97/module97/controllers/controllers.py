# -*- coding: utf-8 -*-
from odoo import http

# class Module97(http.Controller):
#     @http.route('/module97/module97/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module97/module97/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module97.listing', {
#             'root': '/module97/module97',
#             'objects': http.request.env['module97.module97'].search([]),
#         })

#     @http.route('/module97/module97/objects/<model("module97.module97"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module97.object', {
#             'object': obj
#         })