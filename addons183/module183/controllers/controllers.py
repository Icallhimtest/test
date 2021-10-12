# -*- coding: utf-8 -*-
from odoo import http

# class Module183(http.Controller):
#     @http.route('/module183/module183/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module183/module183/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module183.listing', {
#             'root': '/module183/module183',
#             'objects': http.request.env['module183.module183'].search([]),
#         })

#     @http.route('/module183/module183/objects/<model("module183.module183"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module183.object', {
#             'object': obj
#         })