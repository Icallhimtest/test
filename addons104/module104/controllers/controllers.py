# -*- coding: utf-8 -*-
from odoo import http

# class Module104(http.Controller):
#     @http.route('/module104/module104/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module104/module104/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module104.listing', {
#             'root': '/module104/module104',
#             'objects': http.request.env['module104.module104'].search([]),
#         })

#     @http.route('/module104/module104/objects/<model("module104.module104"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module104.object', {
#             'object': obj
#         })