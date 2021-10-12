# -*- coding: utf-8 -*-
from odoo import http

# class Module325(http.Controller):
#     @http.route('/module325/module325/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module325/module325/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module325.listing', {
#             'root': '/module325/module325',
#             'objects': http.request.env['module325.module325'].search([]),
#         })

#     @http.route('/module325/module325/objects/<model("module325.module325"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module325.object', {
#             'object': obj
#         })