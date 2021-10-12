# -*- coding: utf-8 -*-
from odoo import http

# class Module501(http.Controller):
#     @http.route('/module501/module501/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module501/module501/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module501.listing', {
#             'root': '/module501/module501',
#             'objects': http.request.env['module501.module501'].search([]),
#         })

#     @http.route('/module501/module501/objects/<model("module501.module501"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module501.object', {
#             'object': obj
#         })