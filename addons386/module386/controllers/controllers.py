# -*- coding: utf-8 -*-
from odoo import http

# class Module386(http.Controller):
#     @http.route('/module386/module386/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module386/module386/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module386.listing', {
#             'root': '/module386/module386',
#             'objects': http.request.env['module386.module386'].search([]),
#         })

#     @http.route('/module386/module386/objects/<model("module386.module386"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module386.object', {
#             'object': obj
#         })