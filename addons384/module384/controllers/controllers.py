# -*- coding: utf-8 -*-
from odoo import http

# class Module384(http.Controller):
#     @http.route('/module384/module384/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module384/module384/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module384.listing', {
#             'root': '/module384/module384',
#             'objects': http.request.env['module384.module384'].search([]),
#         })

#     @http.route('/module384/module384/objects/<model("module384.module384"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module384.object', {
#             'object': obj
#         })