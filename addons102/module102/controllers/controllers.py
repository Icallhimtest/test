# -*- coding: utf-8 -*-
from odoo import http

# class Module102(http.Controller):
#     @http.route('/module102/module102/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module102/module102/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module102.listing', {
#             'root': '/module102/module102',
#             'objects': http.request.env['module102.module102'].search([]),
#         })

#     @http.route('/module102/module102/objects/<model("module102.module102"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module102.object', {
#             'object': obj
#         })