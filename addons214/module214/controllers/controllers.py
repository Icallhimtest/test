# -*- coding: utf-8 -*-
from odoo import http

# class Module214(http.Controller):
#     @http.route('/module214/module214/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module214/module214/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module214.listing', {
#             'root': '/module214/module214',
#             'objects': http.request.env['module214.module214'].search([]),
#         })

#     @http.route('/module214/module214/objects/<model("module214.module214"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module214.object', {
#             'object': obj
#         })