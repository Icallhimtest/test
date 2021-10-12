# -*- coding: utf-8 -*-
from odoo import http

# class Module413(http.Controller):
#     @http.route('/module413/module413/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module413/module413/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module413.listing', {
#             'root': '/module413/module413',
#             'objects': http.request.env['module413.module413'].search([]),
#         })

#     @http.route('/module413/module413/objects/<model("module413.module413"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module413.object', {
#             'object': obj
#         })