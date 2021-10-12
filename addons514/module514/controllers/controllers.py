# -*- coding: utf-8 -*-
from odoo import http

# class Module514(http.Controller):
#     @http.route('/module514/module514/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module514/module514/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module514.listing', {
#             'root': '/module514/module514',
#             'objects': http.request.env['module514.module514'].search([]),
#         })

#     @http.route('/module514/module514/objects/<model("module514.module514"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module514.object', {
#             'object': obj
#         })