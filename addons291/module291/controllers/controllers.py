# -*- coding: utf-8 -*-
from odoo import http

# class Module291(http.Controller):
#     @http.route('/module291/module291/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module291/module291/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module291.listing', {
#             'root': '/module291/module291',
#             'objects': http.request.env['module291.module291'].search([]),
#         })

#     @http.route('/module291/module291/objects/<model("module291.module291"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module291.object', {
#             'object': obj
#         })