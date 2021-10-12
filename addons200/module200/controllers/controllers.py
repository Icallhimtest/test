# -*- coding: utf-8 -*-
from odoo import http

# class Module200(http.Controller):
#     @http.route('/module200/module200/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module200/module200/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module200.listing', {
#             'root': '/module200/module200',
#             'objects': http.request.env['module200.module200'].search([]),
#         })

#     @http.route('/module200/module200/objects/<model("module200.module200"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module200.object', {
#             'object': obj
#         })