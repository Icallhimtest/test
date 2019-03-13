# -*- coding: utf-8 -*-
from odoo import http

# class Module442(http.Controller):
#     @http.route('/module442/module442/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module442/module442/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module442.listing', {
#             'root': '/module442/module442',
#             'objects': http.request.env['module442.module442'].search([]),
#         })

#     @http.route('/module442/module442/objects/<model("module442.module442"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module442.object', {
#             'object': obj
#         })