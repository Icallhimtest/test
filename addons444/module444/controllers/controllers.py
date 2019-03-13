# -*- coding: utf-8 -*-
from odoo import http

# class Module444(http.Controller):
#     @http.route('/module444/module444/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module444/module444/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module444.listing', {
#             'root': '/module444/module444',
#             'objects': http.request.env['module444.module444'].search([]),
#         })

#     @http.route('/module444/module444/objects/<model("module444.module444"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module444.object', {
#             'object': obj
#         })