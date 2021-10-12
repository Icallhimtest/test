# -*- coding: utf-8 -*-
from odoo import http

# class Module357(http.Controller):
#     @http.route('/module357/module357/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module357/module357/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module357.listing', {
#             'root': '/module357/module357',
#             'objects': http.request.env['module357.module357'].search([]),
#         })

#     @http.route('/module357/module357/objects/<model("module357.module357"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module357.object', {
#             'object': obj
#         })