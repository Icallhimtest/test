# -*- coding: utf-8 -*-
from odoo import http

# class Module493(http.Controller):
#     @http.route('/module493/module493/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module493/module493/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module493.listing', {
#             'root': '/module493/module493',
#             'objects': http.request.env['module493.module493'].search([]),
#         })

#     @http.route('/module493/module493/objects/<model("module493.module493"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module493.object', {
#             'object': obj
#         })