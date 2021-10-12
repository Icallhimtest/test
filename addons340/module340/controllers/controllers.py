# -*- coding: utf-8 -*-
from odoo import http

# class Module340(http.Controller):
#     @http.route('/module340/module340/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module340/module340/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module340.listing', {
#             'root': '/module340/module340',
#             'objects': http.request.env['module340.module340'].search([]),
#         })

#     @http.route('/module340/module340/objects/<model("module340.module340"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module340.object', {
#             'object': obj
#         })