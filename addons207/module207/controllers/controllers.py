# -*- coding: utf-8 -*-
from odoo import http

# class Module207(http.Controller):
#     @http.route('/module207/module207/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module207/module207/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module207.listing', {
#             'root': '/module207/module207',
#             'objects': http.request.env['module207.module207'].search([]),
#         })

#     @http.route('/module207/module207/objects/<model("module207.module207"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module207.object', {
#             'object': obj
#         })