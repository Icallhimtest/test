# -*- coding: utf-8 -*-
from odoo import http

# class Module79(http.Controller):
#     @http.route('/module79/module79/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module79/module79/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module79.listing', {
#             'root': '/module79/module79',
#             'objects': http.request.env['module79.module79'].search([]),
#         })

#     @http.route('/module79/module79/objects/<model("module79.module79"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module79.object', {
#             'object': obj
#         })