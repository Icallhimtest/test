# -*- coding: utf-8 -*-
from odoo import http

# class Module127(http.Controller):
#     @http.route('/module127/module127/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module127/module127/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module127.listing', {
#             'root': '/module127/module127',
#             'objects': http.request.env['module127.module127'].search([]),
#         })

#     @http.route('/module127/module127/objects/<model("module127.module127"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module127.object', {
#             'object': obj
#         })