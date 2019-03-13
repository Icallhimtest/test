# -*- coding: utf-8 -*-
from odoo import http

# class Module441(http.Controller):
#     @http.route('/module441/module441/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module441/module441/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module441.listing', {
#             'root': '/module441/module441',
#             'objects': http.request.env['module441.module441'].search([]),
#         })

#     @http.route('/module441/module441/objects/<model("module441.module441"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module441.object', {
#             'object': obj
#         })