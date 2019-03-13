# -*- coding: utf-8 -*-
from odoo import http

# class Module118(http.Controller):
#     @http.route('/module118/module118/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module118/module118/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module118.listing', {
#             'root': '/module118/module118',
#             'objects': http.request.env['module118.module118'].search([]),
#         })

#     @http.route('/module118/module118/objects/<model("module118.module118"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module118.object', {
#             'object': obj
#         })