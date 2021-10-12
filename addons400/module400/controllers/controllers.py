# -*- coding: utf-8 -*-
from odoo import http

# class Module400(http.Controller):
#     @http.route('/module400/module400/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module400/module400/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module400.listing', {
#             'root': '/module400/module400',
#             'objects': http.request.env['module400.module400'].search([]),
#         })

#     @http.route('/module400/module400/objects/<model("module400.module400"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module400.object', {
#             'object': obj
#         })