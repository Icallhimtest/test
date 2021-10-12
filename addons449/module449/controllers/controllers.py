# -*- coding: utf-8 -*-
from odoo import http

# class Module449(http.Controller):
#     @http.route('/module449/module449/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module449/module449/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module449.listing', {
#             'root': '/module449/module449',
#             'objects': http.request.env['module449.module449'].search([]),
#         })

#     @http.route('/module449/module449/objects/<model("module449.module449"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module449.object', {
#             'object': obj
#         })