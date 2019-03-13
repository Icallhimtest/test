# -*- coding: utf-8 -*-
from odoo import http

# class Module427(http.Controller):
#     @http.route('/module427/module427/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module427/module427/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module427.listing', {
#             'root': '/module427/module427',
#             'objects': http.request.env['module427.module427'].search([]),
#         })

#     @http.route('/module427/module427/objects/<model("module427.module427"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module427.object', {
#             'object': obj
#         })