# -*- coding: utf-8 -*-
from odoo import http

# class Module160(http.Controller):
#     @http.route('/module160/module160/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module160/module160/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module160.listing', {
#             'root': '/module160/module160',
#             'objects': http.request.env['module160.module160'].search([]),
#         })

#     @http.route('/module160/module160/objects/<model("module160.module160"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module160.object', {
#             'object': obj
#         })