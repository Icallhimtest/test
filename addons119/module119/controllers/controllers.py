# -*- coding: utf-8 -*-
from odoo import http

# class Module119(http.Controller):
#     @http.route('/module119/module119/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module119/module119/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module119.listing', {
#             'root': '/module119/module119',
#             'objects': http.request.env['module119.module119'].search([]),
#         })

#     @http.route('/module119/module119/objects/<model("module119.module119"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module119.object', {
#             'object': obj
#         })