# -*- coding: utf-8 -*-
from odoo import http

# class Module436(http.Controller):
#     @http.route('/module436/module436/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module436/module436/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module436.listing', {
#             'root': '/module436/module436',
#             'objects': http.request.env['module436.module436'].search([]),
#         })

#     @http.route('/module436/module436/objects/<model("module436.module436"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module436.object', {
#             'object': obj
#         })