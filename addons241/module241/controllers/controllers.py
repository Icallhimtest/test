# -*- coding: utf-8 -*-
from odoo import http

# class Module241(http.Controller):
#     @http.route('/module241/module241/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module241/module241/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module241.listing', {
#             'root': '/module241/module241',
#             'objects': http.request.env['module241.module241'].search([]),
#         })

#     @http.route('/module241/module241/objects/<model("module241.module241"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module241.object', {
#             'object': obj
#         })