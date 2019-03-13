# -*- coding: utf-8 -*-
from odoo import http

# class Module424(http.Controller):
#     @http.route('/module424/module424/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module424/module424/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module424.listing', {
#             'root': '/module424/module424',
#             'objects': http.request.env['module424.module424'].search([]),
#         })

#     @http.route('/module424/module424/objects/<model("module424.module424"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module424.object', {
#             'object': obj
#         })