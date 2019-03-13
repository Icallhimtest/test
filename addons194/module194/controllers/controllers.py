# -*- coding: utf-8 -*-
from odoo import http

# class Module194(http.Controller):
#     @http.route('/module194/module194/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module194/module194/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module194.listing', {
#             'root': '/module194/module194',
#             'objects': http.request.env['module194.module194'].search([]),
#         })

#     @http.route('/module194/module194/objects/<model("module194.module194"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module194.object', {
#             'object': obj
#         })