# -*- coding: utf-8 -*-
from odoo import http

# class Module258(http.Controller):
#     @http.route('/module258/module258/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module258/module258/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module258.listing', {
#             'root': '/module258/module258',
#             'objects': http.request.env['module258.module258'].search([]),
#         })

#     @http.route('/module258/module258/objects/<model("module258.module258"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module258.object', {
#             'object': obj
#         })