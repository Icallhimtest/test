# -*- coding: utf-8 -*-
from odoo import http

# class Module26(http.Controller):
#     @http.route('/module26/module26/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module26/module26/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module26.listing', {
#             'root': '/module26/module26',
#             'objects': http.request.env['module26.module26'].search([]),
#         })

#     @http.route('/module26/module26/objects/<model("module26.module26"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module26.object', {
#             'object': obj
#         })