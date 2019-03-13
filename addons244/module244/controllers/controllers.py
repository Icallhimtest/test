# -*- coding: utf-8 -*-
from odoo import http

# class Module244(http.Controller):
#     @http.route('/module244/module244/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module244/module244/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module244.listing', {
#             'root': '/module244/module244',
#             'objects': http.request.env['module244.module244'].search([]),
#         })

#     @http.route('/module244/module244/objects/<model("module244.module244"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module244.object', {
#             'object': obj
#         })