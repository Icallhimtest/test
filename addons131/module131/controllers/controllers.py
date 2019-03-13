# -*- coding: utf-8 -*-
from odoo import http

# class Module131(http.Controller):
#     @http.route('/module131/module131/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module131/module131/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module131.listing', {
#             'root': '/module131/module131',
#             'objects': http.request.env['module131.module131'].search([]),
#         })

#     @http.route('/module131/module131/objects/<model("module131.module131"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module131.object', {
#             'object': obj
#         })